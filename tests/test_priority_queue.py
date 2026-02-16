"""
Unit Tests for Priority Queue Implementation
"""

import sys
from pathlib import Path
import unittest

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.priority_queue import Task, PriorityQueue


class TestTask(unittest.TestCase):
    """Tests for Task class."""

    def test_creation(self):
        task = Task(1, priority=5, arrival_time=0.0, deadline=10.0)
        self.assertEqual(task.task_id, 1)
        self.assertEqual(task.priority, 5)

    def test_priority_comparison(self):
        t1 = Task(1, priority=5, arrival_time=0, deadline=10)
        t2 = Task(2, priority=8, arrival_time=0, deadline=10)
        self.assertTrue(t2 > t1)

    def test_deadline_comparison(self):
        t1 = Task(1, priority=5, arrival_time=0, deadline=15)
        t2 = Task(2, priority=5, arrival_time=0, deadline=10)
        self.assertTrue(t2 > t1)  # Earlier deadline wins


class TestPriorityQueue(unittest.TestCase):
    """Tests for PriorityQueue class."""

    def test_empty(self):
        pq = PriorityQueue()
        self.assertTrue(pq.is_empty())
        self.assertIsNone(pq.extract_max())

    def test_insert_single(self):
        pq = PriorityQueue()
        pq.insert(Task(1, priority=5, arrival_time=0, deadline=10))
        self.assertEqual(len(pq), 1)
        self.assertEqual(pq.peek().task_id, 1)

    def test_extract_order(self):
        pq = PriorityQueue()
        pq.insert(Task(1, priority=5, arrival_time=0, deadline=10))
        pq.insert(Task(2, priority=8, arrival_time=1, deadline=12))
        pq.insert(Task(3, priority=3, arrival_time=2, deadline=15))
        
        self.assertEqual(pq.extract_max().priority, 8)
        self.assertEqual(pq.extract_max().priority, 5)
        self.assertEqual(pq.extract_max().priority, 3)

    def test_increase_key(self):
        pq = PriorityQueue()
        pq.insert(Task(1, priority=5, arrival_time=0, deadline=10))
        pq.insert(Task(2, priority=8, arrival_time=1, deadline=12))
        
        pq.increase_key(1, 10)
        self.assertEqual(pq.peek().task_id, 1)

    def test_remove(self):
        pq = PriorityQueue()
        pq.insert(Task(1, priority=5, arrival_time=0, deadline=10))
        pq.insert(Task(2, priority=8, arrival_time=1, deadline=12))
        
        removed = pq.remove(2)
        self.assertEqual(removed.task_id, 2)
        self.assertEqual(len(pq), 1)


if __name__ == '__main__':
    unittest.main(verbosity=2)
