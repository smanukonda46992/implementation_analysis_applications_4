"""
Timing Utilities for Algorithm Benchmarking
"""

import time
from typing import Callable, List, Dict
from dataclasses import dataclass
import statistics


@dataclass
class TimingResult:
    """Results from timing an algorithm."""
    algorithm_name: str
    input_size: int
    distribution: str
    mean_time: float
    std_dev: float
    min_time: float
    max_time: float
    iterations: int


def time_single_run(func: Callable, arr: List[int]) -> float:
    """Time a single execution of a sorting function."""
    arr_copy = arr.copy()
    start = time.perf_counter()
    func(arr_copy)
    return time.perf_counter() - start


def time_algorithm(func: Callable, arr: List[int], 
                   iterations: int = 5, warmup: int = 1) -> Dict[str, float]:
    """Time algorithm with multiple iterations."""
    # Warmup
    for _ in range(warmup):
        time_single_run(func, arr)

    # Timed runs
    times = [time_single_run(func, arr) for _ in range(iterations)]

    return {
        'mean': statistics.mean(times),
        'std': statistics.stdev(times) if len(times) > 1 else 0.0,
        'min': min(times),
        'max': max(times),
    }


def format_timing_table(results: List[TimingResult]) -> str:
    """Format results as readable table."""
    lines = [f"{'Algorithm':<15} {'Size':<10} {'Mean (s)':<12} {'Std Dev':<12}"]
    lines.append("-" * 50)
    for r in results:
        lines.append(f"{r.algorithm_name:<15} {r.input_size:<10} {r.mean_time:<12.6f} {r.std_dev:<12.6f}")
    return "\n".join(lines)
