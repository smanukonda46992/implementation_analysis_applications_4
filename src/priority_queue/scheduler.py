"""
Task Scheduler Simulation using Priority Queue

Demonstrates practical application of the priority queue
in a task scheduling scenario.
"""

from typing import List, Tuple, Optional
from dataclasses import dataclass
from .task import Task
from .priority_queue import PriorityQueue
import random


@dataclass
class SchedulerStats:
    """Statistics from scheduler simulation."""
    total_tasks: int
    completed_tasks: int
    missed_deadlines: int
    average_wait_time: float
    average_turnaround_time: float
    throughput: float


class TaskScheduler:
    """Task scheduler using priority queue for scheduling decisions."""

    def __init__(self):
        self.queue = PriorityQueue()
        self.current_time: float = 0.0
        self.completed: List[Tuple[Task, float, float]] = []

    def add_task(self, task: Task) -> None:
        """Add task to scheduler queue."""
        self.queue.insert(task)

    def process_next(self, processing_time: float = 1.0) -> Optional[Task]:
        """Process highest priority task."""
        task = self.queue.extract_max()
        if task is None:
            return None

        start_time = self.current_time
        self.current_time += processing_time
        self.completed.append((task, start_time, self.current_time))
        return task

    def run_simulation(self, processing_time: float = 1.0) -> SchedulerStats:
        """Process all tasks and return statistics."""
        while not self.queue.is_empty():
            self.process_next(processing_time)
        return self.get_statistics()

    def get_statistics(self) -> SchedulerStats:
        """Calculate scheduling statistics."""
        if not self.completed:
            return SchedulerStats(0, 0, 0, 0.0, 0.0, 0.0)

        total_wait = total_turnaround = missed = 0
        for task, start, end in self.completed:
            total_wait += start - task.arrival_time
            total_turnaround += end - task.arrival_time
            if end > task.deadline:
                missed += 1

        n = len(self.completed)
        return SchedulerStats(
            total_tasks=n,
            completed_tasks=n,
            missed_deadlines=missed,
            average_wait_time=total_wait / n,
            average_turnaround_time=total_turnaround / n,
            throughput=n / max(self.current_time, 1)
        )


def generate_random_tasks(count: int, 
                          priority_range: Tuple[int, int] = (1, 10),
                          deadline_range: Tuple[float, float] = (5.0, 50.0)) -> List[Task]:
    """Generate random tasks for testing."""
    tasks = []
    for i in range(count):
        tasks.append(Task(
            task_id=i + 1,
            priority=random.randint(*priority_range),
            arrival_time=float(i),
            deadline=float(i) + random.uniform(*deadline_range)
        ))
    return tasks


def demo_scheduler():
    """Demonstrate the task scheduler."""
    print("=" * 50)
    print("Task Scheduler Demonstration")
    print("=" * 50)

    scheduler = TaskScheduler()
    
    # Sample tasks
    tasks = [
        Task(1, priority=5, arrival_time=0.0, deadline=10.0),
        Task(2, priority=8, arrival_time=1.0, deadline=15.0),
        Task(3, priority=3, arrival_time=2.0, deadline=8.0),
        Task(4, priority=10, arrival_time=3.0, deadline=20.0),
        Task(5, priority=5, arrival_time=4.0, deadline=12.0),
    ]

    print("\nAdding tasks:")
    for task in tasks:
        print(f"  {task}")
        scheduler.add_task(task)

    print("\nProcessing order:")
    order = 1
    while not scheduler.queue.is_empty():
        task = scheduler.process_next()
        if task:
            print(f"  {order}. {task}")
            order += 1

    stats = scheduler.get_statistics()
    print(f"\nStatistics:")
    print(f"  Completed: {stats.completed_tasks}")
    print(f"  Missed deadlines: {stats.missed_deadlines}")
    print(f"  Avg wait time: {stats.average_wait_time:.2f}")


if __name__ == "__main__":
    demo_scheduler()
