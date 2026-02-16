"""
Heap Operations Module

Core heap operations: heapify and build_max_heap.
Used by Heapsort for in-place sorting.
"""

from typing import List


def heapify(arr: List[int], n: int, i: int) -> None:
    """
    Maintain max-heap property for subtree rooted at index i.
    Time: O(log n), Space: O(log n) due to recursion
    """
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heapify_iterative(arr: List[int], n: int, i: int) -> None:
    """Iterative heapify to avoid stack overflow on large arrays."""
    while True:
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right

        if largest == i:
            break

        arr[i], arr[largest] = arr[largest], arr[i]
        i = largest


def build_max_heap(arr: List[int]) -> None:
    """
    Convert array into max-heap in-place.
    Time: O(n) - not O(n log n) due to heap structure
    """
    n = len(arr)
    # Start from last non-leaf node
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
