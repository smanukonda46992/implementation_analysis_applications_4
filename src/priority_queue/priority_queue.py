"""
Priority Queue using Binary Max-Heap
Author: smanukonda46992
Course: DS Assignment 4

Array-based heap with O(log n) operations.
"""

from typing import List, Optional, Dict, Any
from .task import Task


class PriorityQueue:
    """
    Binary max-heap based priority queue for task scheduling.
    
    Operations:
        insert: O(log n)
        extract_max: O(log n)
        peek: O(1)
        increase/decrease_key: O(log n)
    """

    def __init__(self):
        self.heap: List[Task] = []
        self._index_map: Dict[Any, int] = {}  # task_id -> heap index

    def __len__(self) -> int:
        return len(self.heap)

    def __bool__(self) -> bool:
        return len(self.heap) > 0

    def __repr__(self) -> str:
        if self.is_empty():
            return "PriorityQueue(empty)"
        return f"PriorityQueue(size={len(self)}, max={self.peek()})"

    def __contains__(self, task_id: Any) -> bool:
        return task_id in self._index_map

    def is_empty(self) -> bool:
        """Check if queue is empty. O(1)"""
        return len(self.heap) == 0

    def peek(self) -> Optional[Task]:
        """Return highest priority task without removing. O(1)"""
        if self.is_empty():
            return None
        return self.heap[0]

    def insert(self, task: Task) -> None:
        """Insert task and restore heap property. O(log n)"""
        if task.task_id in self._index_map:
            raise ValueError(f"Task with id {task.task_id} already exists")

        self.heap.append(task)
        idx = len(self.heap) - 1
        self._index_map[task.task_id] = idx
        self._sift_up(idx)

    def extract_max(self) -> Optional[Task]:
        """Remove and return highest priority task. O(log n)"""
        if self.is_empty():
            return None

        root = self.heap[0]
        del self._index_map[root.task_id]

        last = self.heap.pop()
        if not self.is_empty():
            self.heap[0] = last
            self._index_map[last.task_id] = 0
            self._heapify(0)

        return root

    def increase_key(self, task_id: Any, new_priority: int) -> bool:
        """Increase task priority. O(log n)"""
        if task_id not in self._index_map:
            return False

        idx = self._index_map[task_id]
        task = self.heap[idx]

        if new_priority < task.priority:
            raise ValueError("New priority must be >= current priority")

        task.priority = new_priority
        self._sift_up(idx)
        return True

    def decrease_key(self, task_id: Any, new_priority: int) -> bool:
        """Decrease task priority. O(log n)"""
        if task_id not in self._index_map:
            return False

        idx = self._index_map[task_id]
        task = self.heap[idx]

        if new_priority > task.priority:
            raise ValueError("New priority must be <= current priority")

        task.priority = new_priority
        self._heapify(idx)
        return True

    def remove(self, task_id: Any) -> Optional[Task]:
        """Remove specific task by ID. O(log n)"""
        if task_id not in self._index_map:
            return None

        idx = self._index_map[task_id]
        task = self.heap[idx]

        last = self.heap.pop()
        del self._index_map[task.task_id]

        if idx < len(self.heap):
            self.heap[idx] = last
            self._index_map[last.task_id] = idx
            parent = (idx - 1) // 2
            if idx > 0 and self.heap[idx] > self.heap[parent]:
                self._sift_up(idx)
            else:
                self._heapify(idx)

        return task

    def _sift_up(self, idx: int) -> None:
        """Move element up to restore heap property."""
        while idx > 0:
            parent = (idx - 1) // 2
            if self.heap[idx] > self.heap[parent]:
                self._swap(idx, parent)
                idx = parent
            else:
                break

    def _heapify(self, idx: int) -> None:
        """Move element down to restore heap property."""
        n = len(self.heap)
        while True:
            largest = idx
            left = 2 * idx + 1
            right = 2 * idx + 2

            if left < n and self.heap[left] > self.heap[largest]:
                largest = left
            if right < n and self.heap[right] > self.heap[largest]:
                largest = right

            if largest == idx:
                break

            self._swap(idx, largest)
            idx = largest

    def _swap(self, i: int, j: int) -> None:
        """Swap elements and update index map."""
        self._index_map[self.heap[i].task_id] = j
        self._index_map[self.heap[j].task_id] = i
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
