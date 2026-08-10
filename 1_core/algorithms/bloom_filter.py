"""
Bloom Filter
------------
A space-efficient probabilistic data structure used to test whether an
element is "possibly in a set" or "definitely not in a set". Trades a
small, tunable false-positive rate for massive memory savings vs a
hash set. No false negatives are possible.

Typical use in this platform: fast existence checks before hitting the
database (e.g. "has this API key been seen before?") to avoid
unnecessary DB round-trips.
"""

import math
from 1_core.utils.hashing import double_hash  # noqa: E501  (import kept explicit for clarity)


class BloomFilter:
    def __init__(self, expected_items: int, false_positive_rate: float = 0.01):
        # Compute optimal bit array size (m) and number of hash functions (k)
        # using the standard Bloom filter formulas.
        self.size = self._optimal_size(expected_items, false_positive_rate)
        self.hash_count = self._optimal_hash_count(self.size, expected_items)
        self.bit_array = [0] * self.size

    @staticmethod
    def _optimal_size(n: int, p: float) -> int:
        # m = -(n * ln(p)) / (ln(2)^2)
        return max(1, int(-(n * math.log(p)) / (math.log(2) ** 2)))

    @staticmethod
    def _optimal_hash_count(m: int, n: int) -> int:
        # k = (m / n) * ln(2)
        return max(1, int((m / n) * math.log(2)))

    def add(self, item: str) -> None:
        # Set the bit at each of the k hashed positions for this item.
        for seed in range(self.hash_count):
            index = double_hash(item, seed) % self.size
            self.bit_array[index] = 1

    def might_contain(self, item: str) -> bool:
        # If ANY of the k positions is unset, the item is definitely absent.
        # If ALL are set, the item is probably present (small false-positive chance).
        return all(
            self.bit_array[double_hash(item, seed) % self.size] == 1
            for seed in range(self.hash_count)
        )
