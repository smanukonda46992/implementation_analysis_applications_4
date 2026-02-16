"""
Heapsort Module

This module provides the Heapsort algorithm implementation using a binary max-heap.

Exports:
    - heapify: Maintains the max-heap property for a subtree.
    - build_max_heap: Builds a max-heap from an unsorted array.
    - heapsort: Sorts an array in ascending order using Heapsort.
"""

from .heap_operations import heapify, build_max_heap
from .heapsort import heapsort

__all__ = ['heapify', 'build_max_heap', 'heapsort']
