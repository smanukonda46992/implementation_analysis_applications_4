"""
Input Data Generators for Experiments

Generates various input distributions for benchmarking sorting algorithms.
"""

from typing import List
import random
import numpy as np


def generate_random(size: int, min_val: int = 0, max_val: int = 100000) -> List[int]:
    """Generate random integers."""
    return np.random.randint(min_val, max_val + 1, size).tolist()


def generate_sorted(size: int) -> List[int]:
    """Generate sorted array (ascending)."""
    return list(range(size))


def generate_reverse_sorted(size: int) -> List[int]:
    """Generate reverse sorted array (descending)."""
    return list(range(size, 0, -1))


def generate_nearly_sorted(size: int, swap_fraction: float = 0.05) -> List[int]:
    """Generate nearly sorted array with some swaps."""
    arr = list(range(size))
    for _ in range(int(size * swap_fraction)):
        i, j = random.randint(0, size - 1), random.randint(0, size - 1)
        arr[i], arr[j] = arr[j], arr[i]
    return arr


def generate_few_unique(size: int, num_unique: int = 10) -> List[int]:
    """Generate array with limited unique values."""
    values = list(range(num_unique))
    return [random.choice(values) for _ in range(size)]


# Distribution registry
DISTRIBUTIONS = {
    'random': generate_random,
    'sorted': generate_sorted,
    'reverse': generate_reverse_sorted,
    'nearly_sorted': generate_nearly_sorted,
    'few_unique': generate_few_unique,
}


def get_distribution(name: str, size: int) -> List[int]:
    """Get array with specified distribution."""
    if name not in DISTRIBUTIONS:
        raise ValueError(f"Unknown distribution: {name}")
    return DISTRIBUTIONS[name](size)
