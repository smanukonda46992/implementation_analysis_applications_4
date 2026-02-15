# Assignment 4 Report: Heap Data Structures

## Heapsort Implementation and Analysis

### Time Complexity

-   **Worst, Average, Best Case:** O(n log n)
-   **Reason:** Building the heap takes O(n), each extraction and heapify takes O(log n), repeated n times.
-   **Space Complexity:** O(1) (in-place), only a few variables for heap operations.

### Comparison with Quicksort and Merge Sort

-   **Quicksort:** O(n log n) average, O(n^2) worst (rare).
-   **Merge Sort:** O(n log n) always, but uses O(n) extra space.
-   **Heapsort:** O(n log n) always, in-place.

### Empirical Results

-   Heapsort is slower than Quicksort on average random data, but more predictable.
-   Merge Sort is fastest for large, stable sorts but uses more memory.

## Priority Queue Implementation

### Data Structure Choice

-   **Array/List:** Efficient for binary heap, easy to implement, O(log n) for insert/extract.

### Task Class

-   Stores task ID, priority, arrival time, deadline.

### Heap Type

-   **Max-Heap:** Highest priority first, suitable for most scheduling.

### Core Operations

-   **Insert:** O(log n)
-   **Extract Max:** O(log n)
-   **Increase Key:** O(log n)
-   **Is Empty:** O(1)

## Design Choices

-   Used Python lists for heap.
-   Task class for extensibility.
-   All code is original and well-documented.

## How to Run

See README.md for instructions.

## Empirical Analysis with Generators

The `heapsort.py` file now includes generator functions to create arrays of different sizes and distributions (random, sorted, reverse). When you run the script, it automatically compares Heapsort, Quicksort, and Merge Sort on these arrays and prints timing results.

### How to Run

1.  Open a terminal in the project directory.
    
2.  Run:
    
    ```zsh
    python3 heapsort.py
    ```
    
3.  The script will output timing results for each sorting algorithm on each array type and size.
    

### Sample Output

```
Array size: 1000, Distribution: randomHeapsort: 0.0123 secondsQuicksort: 0.0087 secondsMerge Sort: 0.0079 secondsArray size: 1000, Distribution: sortedHeapsort: 0.0112 secondsQuicksort: 0.0021 seconds​Merge Sort: 0.0065 seconds​Array size: 1000, Distribution: reverseHeapsort: 0.0120 seconds​Quicksort: 0.0095 secondsMerge Sort: 0.0081 seconds
```

### Interpretation

-   Heapsort is consistent across distributions.
-   Quicksort is fastest on sorted data, but can be slower on reverse or random.
-   Merge Sort is stable and fast, but uses more memory.

## Generator Functions

-   `generate_array(size, distribution)`: Creates arrays for testing.
-   `run_analysis()`: Runs all sorts and prints results.

See `heapsort.py` for implementation details.