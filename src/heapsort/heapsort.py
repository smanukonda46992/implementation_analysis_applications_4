"""
Heapsort Algorithm Implementation

In-place sorting using binary max-heap.
Time: O(n log n) in all cases, Space: O(1)
"""

from typing import List
from .heap_operations import heapify, build_max_heap


def heapsort(arr: List[int]) -> List[int]:
    """
    Sort array using Heapsort algorithm.
    
    Steps:
    1. Build max-heap from array - O(n)
    2. Extract max elements one by one - O(n log n)
    
    Returns the sorted array (modified in-place).
    """
    n = len(arr)
    if n <= 1:
        return arr

    # Build max-heap
    build_max_heap(arr)

    # Extract elements
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # Move max to end
        heapify(arr, i, 0)  # Restore heap

    return arr


def heapsort_with_stats(arr: List[int]) -> dict:
    """Sort array and return statistics (comparisons, swaps)."""
    comparisons = [0]
    swaps = [0]

    def heapify_counted(arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n:
            comparisons[0] += 1
            if arr[left] > arr[largest]:
                largest = left
        if right < n:
            comparisons[0] += 1
            if arr[right] > arr[largest]:
                largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            swaps[0] += 1
            heapify_counted(arr, n, largest)

    n = len(arr)
    arr_copy = arr.copy()

    # Build heap
    for i in range(n // 2 - 1, -1, -1):
        heapify_counted(arr_copy, n, i)

    # Extract
    for i in range(n - 1, 0, -1):
        arr_copy[0], arr_copy[i] = arr_copy[i], arr_copy[0]
        swaps[0] += 1
        heapify_counted(arr_copy, i, 0)

    return {
        'sorted_array': arr_copy,
        'comparisons': comparisons[0],
        'swaps': swaps[0]
    }
