"""
HyperLogLog (HLL)
-----------------
A probabilistic algorithm for estimating the number of DISTINCT elements
(cardinality) in a very large multiset, using a fixed, tiny amount of
memory regardless of the input size.

Typical use in this platform: "how many unique users hit this endpoint
today?" without storing every user ID.
"""

import math
from 1_core.utils.hashing import hash_to_binary  # noqa: E501


class HyperLogLog:
    def __init__(self, precision: int = 14):
        # precision (p) controls accuracy vs memory: m = 2^p registers.
        self.precision = precision
        self.num_registers = 1 << precision
        self.registers = [0] * self.num_registers
        # Correction constant used in the cardinality estimate formula.
        self.alpha = self._alpha(self.num_registers)

    @staticmethod
    def _alpha(m: int) -> float:
        # Standard HLL bias-correction constant for large m.
        return 0.7213 / (1 + 1.079 / m)

    def add(self, item: str) -> None:
        # Hash the item, use the first `precision` bits to pick a register,
        # and store the position of the leftmost 1-bit in the remaining bits.
        binary = hash_to_binary(item)
        register_index = int(binary[: self.precision], 2)
        remaining_bits = binary[self.precision :]
        leading_zeros = len(remaining_bits) - len(remaining_bits.lstrip("0")) + 1
        self.registers[register_index] = max(self.registers[register_index], leading_zeros)

    def estimate_cardinality(self) -> int:
        # Harmonic mean of the registers, scaled by alpha and m^2.
        raw_estimate = self.alpha * (self.num_registers ** 2) / sum(
            2 ** -r for r in self.registers
        )
        return int(raw_estimate)
