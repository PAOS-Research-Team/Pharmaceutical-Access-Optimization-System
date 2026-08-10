"""
Cuckoo Filter
-------------
Similar goal to a Bloom filter (approximate set membership) but supports
DELETION, which Bloom filters cannot do safely. Uses "cuckoo hashing":
each item gets two candidate buckets, and on collision an existing item
is evicted and re-placed into its alternate bucket.

Typical use in this platform: revocation lists (e.g. blocked tokens)
where entries need to be both added and later removed.
"""

import random
from 1_core.utils.hashing import double_hash  # noqa: E501


class CuckooFilter:
    def __init__(self, capacity: int = 10_000, bucket_size: int = 4, max_kicks: int = 500):
        self.capacity = capacity
        self.bucket_size = bucket_size
        self.max_kicks = max_kicks
        self.buckets = [[] for _ in range(capacity)]

    def _fingerprint(self, item: str) -> str:
        # Small hash "signature" of the item, stored instead of the item itself.
        return str(double_hash(item, seed=1) % 255)

    def _index_pair(self, item: str, fingerprint: str):
        i1 = double_hash(item, seed=0) % self.capacity
        i2 = (i1 ^ double_hash(fingerprint, seed=0)) % self.capacity
        return i1, i2

    def insert(self, item: str) -> bool:
        fingerprint = self._fingerprint(item)
        i1, i2 = self._index_pair(item, fingerprint)

        # Try both candidate buckets first.
        for index in (i1, i2):
            if len(self.buckets[index]) < self.bucket_size:
                self.buckets[index].append(fingerprint)
                return True

        # Both buckets full: evict a random existing fingerprint and
        # relocate it, repeating up to max_kicks times.
        index = random.choice([i1, i2])
        for _ in range(self.max_kicks):
            evict_pos = random.randrange(len(self.buckets[index]))
            fingerprint, self.buckets[index][evict_pos] = self.buckets[index][evict_pos], fingerprint
            index = (index ^ double_hash(fingerprint, seed=0)) % self.capacity
            if len(self.buckets[index]) < self.bucket_size:
                self.buckets[index].append(fingerprint)
                return True

        return False  # Filter considered full.

    def contains(self, item: str) -> bool:
        fingerprint = self._fingerprint(item)
        i1, i2 = self._index_pair(item, fingerprint)
        return fingerprint in self.buckets[i1] or fingerprint in self.buckets[i2]

    def delete(self, item: str) -> bool:
        fingerprint = self._fingerprint(item)
        i1, i2 = self._index_pair(item, fingerprint)
        for index in (i1, i2):
            if fingerprint in self.buckets[index]:
                self.buckets[index].remove(fingerprint)
                return True
        return False
