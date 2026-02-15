"""
Priority Queue Implementation using Binary Heap
Original Python code by [Your Name]
"""

from typing import List, Optional

class Task:
    def __init__(self, task_id: int, priority: int, arrival_time: int, deadline: int):
        self.task_id = task_id
        self.priority = priority
        self.arrival_time = arrival_time
        self.deadline = deadline
    def __lt__(self, other):
        return self.priority < other.priority
    def __repr__(self):
        return f"Task(id={self.task_id}, priority={self.priority})"

class PriorityQueue:
    def __init__(self):
        self.heap: List[Task] = []
    def is_empty(self) -> bool:
        return len(self.heap) == 0
    def insert(self, task: Task):
        self.heap.append(task)
        self._sift_up(len(self.heap) - 1)
    def extract_max(self) -> Optional[Task]:
        if self.is_empty():
            return None
        max_task = self.heap[0]
        last_task = self.heap.pop()
        if not self.is_empty():
            self.heap[0] = last_task
            self._heapify(0)
        return max_task
    def increase_key(self, index: int, new_priority: int):
        if index < 0 or index >= len(self.heap):
            return
        if new_priority < self.heap[index].priority:
            return
        self.heap[index].priority = new_priority
        self._sift_up(index)
    def _sift_up(self, idx):
        parent = (idx - 1) // 2
        while idx > 0 and self.heap[idx].priority > self.heap[parent].priority:
            self.heap[idx], self.heap[parent] = self.heap[parent], self.heap[idx]
            idx = parent
            parent = (idx - 1) // 2
    def _heapify(self, idx):
        n = len(self.heap)
        largest = idx
        left = 2 * idx + 1
        right = 2 * idx + 2
        if left < n and self.heap[left].priority > self.heap[largest].priority:
            largest = left
        if right < n and self.heap[right].priority > self.heap[largest].priority:
            largest = right
        if largest != idx:
            self.heap[idx], self.heap[largest] = self.heap[largest], self.heap[idx]
            self._heapify(largest)
    def __repr__(self):
        return f"PriorityQueue({self.heap})"

if __name__ == "__main__":
    pq = PriorityQueue()
    pq.insert(Task(1, 5, 0, 10))
    pq.insert(Task(2, 8, 1, 12))
    pq.insert(Task(3, 3, 2, 15))
    print("Queue:", pq)
    print("Extracted max:", pq.extract_max())
    print("Queue after extraction:", pq)
