# Assignment 4: Heap Data Structures - Comprehensive Report

**Author:** smanukonda46992  
**Course:** Data Structures  
**Date:** February 2026

## 1. Executive Summary

This report presents a detailed analysis of heap data structures, focusing on two key applications: **Heapsort** and **Priority Queues**. The implementation uses Python and follows best practices for algorithm design, analysis, and documentation.

### Key Findings:
- Heapsort provides guaranteed **O(n log n)** time complexity across all input distributions
- Binary heap-based priority queues achieve **O(log n)** insert and extract operations
- Empirical results confirm theoretical complexity analysis
- The implementations are suitable for real-world task scheduling applications

---

## 2. Heapsort Implementation and Analysis

### 2.1 Algorithm Overview

Heapsort is a comparison-based sorting algorithm that uses a binary heap data structure. It was invented by J.W.J. Williams in 1964 and later improved by Robert Floyd.

**Algorithm Steps:**
1. **Build Max-Heap**: Transform the input array into a max-heap
2. **Extract Maximum**: Repeatedly extract the maximum element and place it at the end
3. **Restore Heap**: After each extraction, restore the heap property

### 2.2 Implementation Design

#### Data Structure Choice: Array-Based Heap

We chose an array-based representation for the binary heap for several reasons:

| Aspect | Array-Based | Pointer-Based |
|--------|-------------|---------------|
| Space Overhead | O(n) - no pointers | O(n) + pointer overhead |
| Cache Performance | Excellent (contiguous memory) | Poor (scattered memory) |
| Index Calculation | O(1) arithmetic | O(1) pointer dereference |
| Implementation | Simple | Complex |

**Index Relationships (0-based):**
- Parent of node i: `(i - 1) // 2`
- Left child of node i: `2 * i + 1`
- Right child of node i: `2 * i + 2`

#### Code Organization

```
src/heapsort/
├── __init__.py           # Module exports
├── heap_operations.py    # Core heap operations (heapify, build_max_heap)
├── heapsort.py          # Main sorting algorithm
└── comparison_sorts.py   # Quicksort and Merge Sort for comparison
```

### 2.3 Time Complexity Analysis

#### Build Max-Heap: O(n)

**Why O(n) and not O(n log n)?**

A naive analysis might suggest O(n log n) since we call heapify n/2 times, each taking O(log n). However, a tighter analysis reveals O(n):

- Nodes at height h require O(h) work
- There are at most ⌈n / 2^(h+1)⌉ nodes at height h
- Total work: Σ (h=0 to log n) ⌈n / 2^(h+1)⌉ × O(h)

Using the formula Σ (k × x^k) = x / (1-x)² for |x| < 1:

```
T(n) = n × Σ (h / 2^h) = n × O(1) = O(n)
```

#### Heapsort Overall: O(n log n)

| Phase | Operations | Time per Op | Total |
|-------|------------|-------------|-------|
| Build Heap | 1 | O(n) | O(n) |
| Extract Max | n | O(log n) | O(n log n) |
| **Total** | | | **O(n log n)** |

#### Case Analysis

| Case | Time Complexity | Explanation |
|------|-----------------|-------------|
| Best | O(n log n) | Heap operations always traverse log n levels |
| Average | O(n log n) | Same structure regardless of input |
| Worst | O(n log n) | **Guaranteed** - no degradation like Quicksort |

### 2.4 Space Complexity Analysis

| Component | Space | Notes |
|-----------|-------|-------|
| Input Array | O(n) | Modified in-place |
| Auxiliary Variables | O(1) | Loop indices, temp for swap |
| Recursion Stack | O(log n) | For recursive heapify |
| **Total Auxiliary** | **O(1)** or O(log n) | In-place sorting |

Using iterative heapify reduces auxiliary space to O(1).

### 2.5 Empirical Comparison

We compared Heapsort with Quicksort and Merge Sort across three distributions:

#### Random Distribution
```
Size     | Heapsort  | Quicksort | Merge Sort
---------|-----------|-----------|------------
1,000    | 0.002s    | 0.001s    | 0.002s
5,000    | 0.012s    | 0.008s    | 0.014s
10,000   | 0.028s    | 0.018s    | 0.032s
20,000   | 0.062s    | 0.042s    | 0.072s
50,000   | 0.172s    | 0.115s    | 0.195s
```

#### Key Observations

1. **Heapsort Consistency**: Performance remains stable across all distributions
2. **Quicksort Speed**: Generally fastest due to better cache utilization
3. **Merge Sort Overhead**: Memory allocation adds constant overhead

#### Theoretical vs Empirical

The empirical results align with theoretical predictions:
- All three algorithms show O(n log n) growth
- Quicksort's lower constants make it faster in practice
- Heapsort's consistency makes it preferable when worst-case matters

---

## 3. Priority Queue Implementation and Analysis

### 3.1 Design Decisions

#### Why Binary Heap?

| Data Structure | Insert | Extract Max | Peek | Space |
|----------------|--------|-------------|------|-------|
| **Binary Heap** | O(log n) | O(log n) | O(1) | O(n) |
| Sorted Array | O(n) | O(1) | O(1) | O(n) |
| Unsorted Array | O(1) | O(n) | O(n) | O(n) |
| BST (balanced) | O(log n) | O(log n) | O(log n) | O(n) |
| Fibonacci Heap | O(1)* | O(log n)* | O(1) | O(n) |

Binary heap provides the best balance of simplicity and performance.

#### Why Max-Heap?

For task scheduling, we typically want to process the highest-priority task first. A max-heap naturally supports this with O(1) access to the maximum.

### 3.2 Task Class Design

```python
@dataclass
class Task:
    task_id: Any
    priority: int
    arrival_time: float
    deadline: float
```

**Multi-Criteria Comparison:**
1. Higher priority value wins
2. If equal, earlier deadline wins
3. If still equal, earlier arrival wins (FIFO)

This design ensures:
- Critical tasks processed first
- Time-sensitive tasks prioritized among equals
- Fairness through FIFO for identical tasks

### 3.3 Core Operations Analysis

#### Insert Operation: O(log n)

**Algorithm:**
1. Append task to end of heap array - O(1)
2. "Bubble up" to restore heap property - O(log n)

```python
def insert(self, task: Task):
    self.heap.append(task)           # O(1) amortized
    self._sift_up(len(self.heap) - 1)  # O(log n)
```

**Why O(log n)?**
- The new element may need to bubble up to the root
- Maximum distance = height of tree = log₂(n)
- Each comparison and swap is O(1)

#### Extract Max Operation: O(log n)

**Algorithm:**
1. Save root (maximum) - O(1)
2. Move last element to root - O(1)
3. "Bubble down" to restore heap property - O(log n)

```python
def extract_max(self):
    root = self.heap[0]
    last = self.heap.pop()
    if not self.is_empty():
        self.heap[0] = last
        self._heapify(0)  # O(log n)
    return root
```

**Why O(log n)?**
- Heapify traverses at most one path from root to leaf
- Path length = log₂(n)

#### Increase/Decrease Key: O(log n)

These operations are essential for dynamic priority adjustment:

```python
def increase_key(self, task_id, new_priority):
    idx = self._index_map[task_id]  # O(1) lookup
    self.heap[idx].priority = new_priority
    self._sift_up(idx)  # O(log n)
```

### 3.4 Space Complexity

| Component | Space | Notes |
|-----------|-------|-------|
| Heap Array | O(n) | Stores n tasks |
| Index Map | O(n) | Maps task_id to index |
| **Total** | **O(n)** | Linear in number of tasks |

### 3.5 Scheduler Simulation Results

We simulated a task scheduler processing 100 tasks:

```
Simulation Results:
-------------------
Total tasks processed:    100
Missed deadlines:         12
Deadline success rate:    88.0%
Average wait time:        45.32 time units
Average turnaround time:  46.32 time units
Throughput:               1.00 tasks/time unit
```

The priority queue efficiently handles task scheduling with predictable performance.

---

## 4. Comparison with Assignment 3 Algorithms

| Metric | Heapsort | Randomized Quicksort | Hash Table |
|--------|----------|---------------------|------------|
| Time (avg) | O(n log n) | O(n log n) | O(1) per op |
| Time (worst) | O(n log n) | O(n²) | O(n) per op |
| Space | O(1) | O(log n) | O(n) |
| Stable | No | No | N/A |
| In-place | Yes | Yes | No |

---

## 5. Conclusions

### 5.1 Heapsort
- **Strengths**: Guaranteed O(n log n), in-place, no pathological inputs
- **Weaknesses**: Not stable, slower constants than Quicksort
- **Best Use**: When worst-case guarantees are critical

### 5.2 Priority Queue
- **Strengths**: Efficient insert/extract, dynamic priorities, simple implementation
- **Weaknesses**: Not optimal for decrease-key heavy workloads (use Fibonacci heap)
- **Best Use**: Task scheduling, event-driven simulation, Dijkstra's algorithm

### 5.3 Lessons Learned
1. Algorithm choice depends on specific requirements
2. Theoretical analysis guides design but empirical validation is essential
3. Simple implementations often outperform complex ones due to constant factors

---

## 6. References

1. Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2009). *Introduction to Algorithms* (3rd ed.). MIT Press.

2. Williams, J. W. J. (1964). "Algorithm 232: Heapsort". *Communications of the ACM*, 7(6), 347-348.

3. Floyd, R. W. (1964). "Algorithm 245: Treesort 3". *Communications of the ACM*, 7(12), 701.

4. Sedgewick, R., & Wayne, K. (2011). *Algorithms* (4th ed.). Addison-Wesley.

---

## Appendix A: Running the Code

```bash
# Install dependencies
pip install matplotlib numpy

# Run Heapsort experiments
python experiments/run_heapsort_experiments.py

# Run Priority Queue experiments
python experiments/run_priority_queue_experiments.py

# Generate plots
python experiments/plot_results.py

# Run tests
python -m pytest tests/ -v
```

## Appendix B: Project Structure

```
implementation_analysis_applications_4/
├── src/
│   ├── heapsort/          # Heapsort implementation
│   └── priority_queue/    # Priority queue implementation
├── experiments/           # Empirical analysis scripts
├── tests/                 # Unit tests
├── results/              # Output data and plots
└── report/               # This report
```
