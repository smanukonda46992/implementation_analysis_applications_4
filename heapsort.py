"""
Heapsort Implementation for Assignment 4
Original Python code by [Your Name]
"""

from typing import List, Callable
import random
import time
import matplotlib.pyplot as plt
import numpy as np

def heapify(arr: List[int], n: int, i: int):
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

def heapsort(arr: List[int]) -> List[int]:
    n = len(arr)
    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    # Extract elements
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
    return arr

def generate_array(size: int, distribution: str = 'random') -> list:
    if distribution == 'random':
        return np.random.randint(0, 100000, size).tolist()
    elif distribution == 'sorted':
        return list(range(size))
    elif distribution == 'reverse':
        return list(range(size, 0, -1))
    else:
        raise ValueError('Unknown distribution')

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def mergesort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def time_sort(sort_fn: Callable, arr: list) -> float:
    start = time.perf_counter()
    sort_fn(arr.copy())
    return time.perf_counter() - start

def run_analysis():
    sizes = [1000, 5000, 10000, 20000]
    distributions = ['random', 'sorted', 'reverse']
    sorts = [
        ('Heapsort', heapsort),
        ('Quicksort', quicksort),
        ('Merge Sort', mergesort)
    ]
    stats = {}
    for dist in distributions:
        stats[dist] = {name: [] for name, _ in sorts}
        for size in sizes:
            arr = generate_array(size, dist)
            for name, fn in sorts:
                t = time_sort(fn, arr)
                stats[dist][name].append(t)
                print(f"{name} | size={size} | {dist}: {t:.4f} sec")
    # Plotting
    for dist in distributions:
        plt.figure(figsize=(8,5))
        for name in stats[dist]:
            plt.plot(sizes, stats[dist][name], marker='o', label=name)
        plt.title(f'Sorting Time vs Size ({dist})')
        plt.xlabel('Array Size')
        plt.ylabel('Time (seconds)')
        plt.legend()
        plt.grid(True)
        imgfile = f'analysis_{dist}.png'
        plt.savefig(imgfile)
        print(f"Saved plot: {imgfile}")
    return stats

if __name__ == "__main__":
    run_analysis()
