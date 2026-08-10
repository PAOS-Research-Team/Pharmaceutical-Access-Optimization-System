"""
Bitwise operation helpers
--------------------------
Small, well-tested bit-manipulation helpers used across the
probabilistic data structures (leading-zero counts, bit setting, etc).
"""


def count_leading_zeros(binary_string: str) -> int:
    """Count leading zero bits before the first 1, plus one (HLL convention)."""
    stripped = binary_string.lstrip("0")
    if not stripped:
        return len(binary_string) + 1
    return len(binary_string) - len(stripped) + 1


def set_bit(value: int, position: int) -> int:
    """Return `value` with the bit at `position` set to 1."""
    return value | (1 << position)


def get_bit(value: int, position: int) -> int:
    """Return the bit at `position` in `value` (0 or 1)."""
    return (value >> position) & 1
