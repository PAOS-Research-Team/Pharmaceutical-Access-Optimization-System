"""
Hashing utilities
-----------------
Shared hash functions used by the probabilistic structures in
1_core/algorithms/. Centralized here so every algorithm hashes
consistently and can be swapped out in one place if needed.
"""

import hashlib


def double_hash(item: str, seed: int = 0) -> int:
    """
    Deterministic hash of `item` salted with `seed`, returned as an int.
    Used to simulate multiple independent hash functions from one
    hash algorithm (needed by Bloom/Cuckoo filters).
    """
    digest = hashlib.sha256(f"{seed}:{item}".encode("utf-8")).hexdigest()
    return int(digest, 16)


def hash_to_binary(item: str, bits: int = 32) -> str:
    """Hash `item` and return a fixed-width binary string (used by HLL)."""
    digest = hashlib.sha256(item.encode("utf-8")).hexdigest()
    return bin(int(digest, 16))[2 : 2 + bits].zfill(bits)
