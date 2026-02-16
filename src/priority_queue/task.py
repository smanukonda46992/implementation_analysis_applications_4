"""
Task Class for Priority Queue
Author: smanukonda46992
Course: DS Assignment 4

Schedulable task with priority-based comparison.
"""

from dataclasses import dataclass
from typing import Any, Optional


@dataclass
class Task:
    """
    A task with priority information for scheduling.
    
    Attributes:
        task_id: Unique identifier
        priority: Higher value = more important
        arrival_time: When task was added
        deadline: When task must complete
    """
    task_id: Any
    priority: int
    arrival_time: float
    deadline: float
    description: Optional[str] = None

    def __lt__(self, other: 'Task') -> bool:
        """Compare tasks for heap ordering (lower priority = less than)."""
        if not isinstance(other, Task):
            return NotImplemented
        if self.priority != other.priority:
            return self.priority < other.priority
        if self.deadline != other.deadline:
            return self.deadline > other.deadline  # Earlier deadline is "greater"
        return self.arrival_time > other.arrival_time

    def __gt__(self, other: 'Task') -> bool:
        if not isinstance(other, Task):
            return NotImplemented
        return other < self

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Task):
            return NotImplemented
        return self.task_id == other.task_id

    def __le__(self, other: 'Task') -> bool:
        return self < other or self == other

    def __ge__(self, other: 'Task') -> bool:
        return self > other or self == other

    def __hash__(self) -> int:
        return hash(self.task_id)

    def __repr__(self) -> str:
        return f"Task(id={self.task_id}, priority={self.priority})"

    def __str__(self) -> str:
        return f"Task #{self.task_id} [P:{self.priority}]"

    def is_overdue(self, current_time: float) -> bool:
        """Check if task missed its deadline."""
        return current_time > self.deadline

    def time_until_deadline(self, current_time: float) -> float:
        """Get remaining time until deadline."""
        return self.deadline - current_time
