# Assignment 4: Heap Data Structures - Implementation, Analysis, and Applications

## 📋 Overview

This project provides a comprehensive implementation and analysis of heap data structures, focusing on:
1. **Heapsort Algorithm** - An efficient, in-place sorting algorithm with O(n log n) guaranteed performance
2. **Priority Queue** - A binary heap-based data structure for task scheduling applications

The implementation follows software engineering best practices with modular code organization, extensive documentation, and empirical analysis.

> 📖 **[View the Complete Analysis Report →](analysis_report.md)**  
> For in-depth theoretical analysis, empirical results, and detailed discussion.

---

## 📁 Project Structure

```
implementation_analysis_applications_4/
├── src/                          # Source code modules
│   ├── heapsort/                 # Heapsort implementation
│   │   ├── __init__.py          # Module exports
│   │   ├── heap_operations.py   # Core heap operations (heapify, build_max_heap)
│   │   ├── heapsort.py          # Main sorting algorithm
│   │   └── comparison_sorts.py  # Quicksort & Merge Sort for comparison
│   └── priority_queue/          # Priority Queue implementation
│       ├── __init__.py          # Module exports
│       ├── task.py              # Task class with multi-criteria comparison
│       ├── priority_queue.py    # Binary heap-based priority queue
│       └── scheduler.py         # Task scheduler simulation
├── experiments/                  # Empirical analysis
│   ├── input_generators.py      # Test data generators
│   ├── timing_utils.py          # Benchmarking utilities
│   ├── run_heapsort_experiments.py
│   ├── run_priority_queue_experiments.py
│   └── plot_results.py          # Visualization generation
├── tests/                        # Unit tests
│   ├── test_heapsort.py
│   └── test_priority_queue.py
├── results/                      # Output data and plots
│   ├── plots/
│   └── raw_data/
├── report/                       # Detailed analysis report
│   └── assignment4_report.md
└── README.md                     # This file
```

---

## 🚀 Getting Started

### Prerequisites

```bash
# Python 3.8+ required
python --version

# Install dependencies
pip install matplotlib numpy
```

### Running the Code

```bash
# Run Heapsort experiments with empirical analysis
python experiments/run_heapsort_experiments.py

# Run Priority Queue experiments
python experiments/run_priority_queue_experiments.py

# Generate visualization plots
python experiments/plot_results.py

# Run unit tests
python -m pytest tests/ -v

# Or run tests individually
python tests/test_heapsort.py
python tests/test_priority_queue.py
```

---

## 📊 Part 1: Heapsort Implementation and Analysis

### Design & Implementation

**Data Structure Choice: Array-Based Binary Heap**

We use a Python list to represent the binary heap for several reasons:

| Aspect | Array-Based | Pointer-Based |
|--------|-------------|---------------|
| Space Overhead | O(n) - no pointers | O(n) + pointer overhead |
| Cache Performance | Excellent (contiguous) | Poor (scattered) |
| Index Calculation | O(1) arithmetic | O(1) dereference |
| Implementation | Simple | Complex |

**Index Relationships (0-based):**
- Parent of node i: `(i - 1) // 2`
- Left child of node i: `2 * i + 1`
- Right child of node i: `2 * i + 2`

### Algorithm Steps

```python
def heapsort(arr):
    # Step 1: Build max-heap - O(n)
    build_max_heap(arr)
    
    # Step 2: Extract elements - O(n log n)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # Swap max to end
        heapify(arr, i, 0)                # Restore heap property
    
    return arr
```

### Time Complexity Analysis

| Phase | Operations | Time per Op | Total |
|-------|------------|-------------|-------|
| Build Heap | 1 | O(n) | O(n) |
| Extract Max | n | O(log n) | O(n log n) |
| **Total** | | | **O(n log n)** |

**Why Build Heap is O(n), not O(n log n):**
- Nodes at height h require O(h) work
- There are ⌈n / 2^(h+1)⌉ nodes at height h
- Sum: Σ (n / 2^(h+1)) × O(h) = O(n)

**Case Analysis:**

| Case | Complexity | Explanation |
|------|------------|-------------|
| Best | O(n log n) | Heap operations always O(log n) |
| Average | O(n log n) | Structure independent of input |
| Worst | O(n log n) | **Guaranteed** - no degradation |

### Space Complexity

- **Auxiliary Space:** O(1) - in-place sorting
- **Stack Space:** O(log n) for recursive heapify (O(1) if iterative)

### Empirical Comparison Results

| Distribution | Heapsort | Quicksort | Merge Sort |
|--------------|----------|-----------|------------|
| Random | Consistent | Fastest | Stable |
| Sorted | Consistent | Good* | Consistent |
| Reverse | Consistent | Good* | Consistent |

*With middle-pivot selection

---

## 📊 Part 2: Priority Queue Implementation

### Design Decisions

**Why Binary Heap?**

| Structure | Insert | Extract | Peek | Space |
|-----------|--------|---------|------|-------|
| **Binary Heap** | O(log n) | O(log n) | O(1) | O(n) |
| Sorted Array | O(n) | O(1) | O(1) | O(n) |
| Unsorted Array | O(1) | O(n) | O(n) | O(n) |

**Why Max-Heap?**
- Task scheduling requires highest-priority-first processing
- Max-heap provides O(1) access to maximum priority task

### Task Class Design

```python
@dataclass
class Task:
    task_id: Any
    priority: int           # Higher = more important
    arrival_time: float     # When task entered queue
    deadline: float         # When task must complete
```

**Multi-Criteria Comparison (in order):**
1. Higher priority value wins
2. Earlier deadline wins (among equal priorities)
3. Earlier arrival wins (FIFO for identical tasks)

### Core Operations

| Operation | Time | Description |
|-----------|------|-------------|
| `insert(task)` | O(log n) | Add task, bubble up to restore heap |
| `extract_max()` | O(log n) | Remove max, heapify down |
| `peek()` | O(1) | View max without removal |
| `is_empty()` | O(1) | Check if queue empty |
| `increase_key()` | O(log n) | Increase priority, bubble up |
| `decrease_key()` | O(log n) | Decrease priority, heapify down |
| `remove(id)` | O(log n) | Remove specific task |

### Time Complexity Justification

**Insert - O(log n):**
- New element appended to end: O(1)
- Bubble up at most log₂(n) levels: O(log n)

**Extract Max - O(log n):**
- Save root, replace with last element: O(1)
- Heapify down at most log₂(n) levels: O(log n)

### Scheduler Simulation

The priority queue is demonstrated in a task scheduling scenario:

```
Sample Results (100 tasks):
- Deadline success rate: 88%
- Average wait time: 45.32 units
- Throughput: 1.0 tasks/unit
```

---

## 🧪 Testing

Comprehensive unit tests verify:
- Basic operations (insert, extract, peek)
- Edge cases (empty queue, single element, duplicates)
- Heap property maintenance
- Multi-criteria comparison
- Large-scale correctness

```bash
# Run all tests with verbose output
python -m pytest tests/ -v

# Run specific test file
python tests/test_heapsort.py
python tests/test_priority_queue.py
```

---

## 📈 Results and Findings

### Key Observations

1. **Heapsort Consistency**
   - O(n log n) performance regardless of input distribution
   - No pathological cases unlike Quicksort

2. **Priority Queue Efficiency**
   - Logarithmic operations scale well
   - Index map enables O(1) task lookup for updates

3. **Practical Applications**
   - OS process scheduling
   - Network packet prioritization
   - Event-driven simulation

### Comparison Summary

| Algorithm | Best | Average | Worst | Space | Stable |
|-----------|------|---------|-------|-------|--------|
| Heapsort | O(n log n) | O(n log n) | O(n log n) | O(1) | No |
| Quicksort | O(n log n) | O(n log n) | O(n²) | O(log n) | No |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes |

---

## 📑 Documentation

| Document | Description |
|----------|-------------|
| [📊 Analysis Report](analysis_report.md) | Comprehensive analysis with theoretical proofs, empirical results, and detailed discussion |
| [📘 Detailed Report](report/assignment4_report.md) | Extended report with appendices and references |
| [📋 Assignment](assignment.txt) | Original assignment instructions |

---

## 📚 References

1. Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2009). *Introduction to Algorithms* (3rd ed.). MIT Press.

2. Williams, J. W. J. (1964). "Algorithm 232: Heapsort". *Communications of the ACM*.

3. Sedgewick, R., & Wayne, K. (2011). *Algorithms* (4th ed.). Addison-Wesley.

---

## 📄 License

This project is submitted as part of academic coursework.