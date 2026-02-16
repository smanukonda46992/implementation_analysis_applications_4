"""
Comparison Sorting Algorithms

Quicksort and Merge Sort implementations for empirical comparison with Heapsort.
"""

from typing import List


def quicksort(arr: List[int]) -> List[int]:
    """
    Quicksort with middle-element pivot.
    Time: O(n log n) average, O(n²) worst
    Space: O(n) - not in-place
    """
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quicksort(left) + middle + quicksort(right)


def quicksort_inplace(arr: List[int], low: int = None, high: int = None) -> List[int]:
    """In-place Quicksort using Lomuto partition."""
    if low is None:
        low = 0
    if high is None:
        high = len(arr) - 1

    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    if low < high:
        pi = partition(arr, low, high)
        quicksort_inplace(arr, low, pi - 1)
        quicksort_inplace(arr, pi + 1, high)

    return arr


def mergesort(arr: List[int]) -> List[int]:
    """
    Merge Sort - stable, O(n log n) all cases.
    Space: O(n) for merging.
    """
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])

    # Merge
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])

    return result
