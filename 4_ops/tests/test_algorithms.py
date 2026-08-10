"""
Unit + integration tests
---------------------------
Unit tests target the pure algorithms in 1_core (fast, no I/O).
Integration tests (marked separately) would target 2_backend/api
endpoints against a test DB. Run with: pytest 4_ops/tests
"""

from 1_core.algorithms.bloom_filter import BloomFilter
from 1_core.algorithms.hyperloglog import HyperLogLog
from 1_core.algorithms.cuckoo_filter import CuckooFilter


def test_bloom_filter_no_false_negatives():
    bloom = BloomFilter(expected_items=100)
    bloom.add("alpha")
    # An item that was added must NEVER report "not present".
    assert bloom.might_contain("alpha") is True


def test_hyperloglog_estimate_is_reasonable():
    hll = HyperLogLog(precision=10)
    for i in range(1000):
        hll.add(f"item-{i}")
    estimate = hll.estimate_cardinality()
    # Allow generous tolerance since HLL is an approximation.
    assert 700 < estimate < 1300


def test_cuckoo_filter_insert_contains_delete():
    cuckoo = CuckooFilter(capacity=100)
    assert cuckoo.insert("token-123") is True
    assert cuckoo.contains("token-123") is True
    assert cuckoo.delete("token-123") is True
    assert cuckoo.contains("token-123") is False
