"""
Unit Tests for Heapsort Implementation
"""

import sys
from pathlib import Path
import unittest
import random

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.heapsort import heapsort, heapify, build_max_heap


class TestHeapify(unittest.TestCase):
    """Tests for heapify function."""

    def test_single_swap(self):
        arr = [1, 10, 5]
        heapify(arr, len(arr), 0)
        self.assertEqual(arr[0], 10)

    def test_no_swap_needed(self):
        arr = [10, 5, 3]
        heapify(arr, len(arr), 0)
        self.assertEqual(arr, [10, 5, 3])


class TestBuildMaxHeap(unittest.TestCase):
    """Tests for build_max_heap function."""

    def test_random_array(self):
        arr = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
        build_max_heap(arr)
        self.assertEqual(arr[0], max(arr))

    def test_sorted_array(self):
        arr = list(range(1, 11))
        build_max_heap(arr)
        self.assertEqual(arr[0], 10)


class TestHeapsort(unittest.TestCase):
    """Tests for heapsort function."""

    def test_empty(self):
        self.assertEqual(heapsort([]), [])

    def test_single(self):
        self.assertEqual(heapsort([42]), [42])

    def test_random(self):
        arr = [64, 34, 25, 12, 22, 11, 90]
        self.assertEqual(heapsort(arr), sorted(arr))

    def test_sorted(self):
        arr = list(range(1, 11))
        self.assertEqual(heapsort(arr.copy()), arr)

    def test_reverse(self):
        arr = list(range(10, 0, -1))
        self.assertEqual(heapsort(arr), list(range(1, 11)))

    def test_duplicates(self):
        arr = [5, 2, 8, 2, 9, 1, 5, 8]
        self.assertEqual(heapsort(arr), sorted(arr))

    def test_large(self):
        arr = [random.randint(0, 10000) for _ in range(1000)]
        self.assertEqual(heapsort(arr.copy()), sorted(arr))


if __name__ == '__main__':
    unittest.main(verbosity=2)
