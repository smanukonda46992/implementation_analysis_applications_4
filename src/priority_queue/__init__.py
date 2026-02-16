"""
Priority Queue Module

This module provides a priority queue implementation using a binary max-heap,
optimized for task scheduling applications.

Exports:
    - Task: A class representing a schedulable task with priority.
    - PriorityQueue: Binary heap-based priority queue implementation.

Design Philosophy:
------------------
- Max-heap structure ensures highest priority tasks are extracted first.
- Supports multi-criteria prioritization (priority, deadline, arrival time).
- All operations maintain the heap invariant.
"""

from .task import Task
from .priority_queue import PriorityQueue

__all__ = ['Task', 'PriorityQueue']
