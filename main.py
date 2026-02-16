#!/usr/bin/env python3
"""
Assignment 4: Heap Data Structures
Author: smanukonda46992

Usage: python main.py [all|heapsort|pqueue|demo|tests]
"""

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent
sys.path.insert(0, str(PROJECT_ROOT))


def run_heapsort_experiments():
    """Run Heapsort comparison experiments."""
    print("\n" + "=" * 50)
    print("HEAPSORT EXPERIMENTS")
    print("=" * 50)
    from experiments.run_heapsort_experiments import run_experiments
    run_experiments()


def run_priority_queue_experiments():
    """Run Priority Queue experiments."""
    print("\n" + "=" * 50)
    print("PRIORITY QUEUE EXPERIMENTS")
    print("=" * 50)
    from experiments.run_priority_queue_experiments import main as pq_main
    pq_main()


def run_tests():
    """Run unit tests."""
    print("\n" + "=" * 50)
    print("UNIT TESTS")
    print("=" * 50)
    import unittest
    loader = unittest.TestLoader()
    suite = loader.discover('tests', pattern='test_*.py')
    runner = unittest.TextTestRunner(verbosity=2)
    return runner.run(suite).wasSuccessful()


def run_demo():
    """Run demonstrations."""
    print("\n" + "=" * 50)
    print("HEAPSORT DEMO")
    print("=" * 50)
    
    from src.heapsort import heapsort
    arr = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original: {arr}")
    print(f"Sorted:   {heapsort(arr.copy())}")
    
    print("\n" + "=" * 50)
    print("PRIORITY QUEUE DEMO")
    print("=" * 50)
    from src.priority_queue.scheduler import demo_scheduler
    demo_scheduler()


def main():
    """Main entry point."""
    print("=" * 50)
    print("Assignment 4: Heap Data Structures")
    print("=" * 50)
    
    command = sys.argv[1] if len(sys.argv) > 1 else 'all'
    
    if command == 'all':
        run_demo()
        run_heapsort_experiments()
        run_priority_queue_experiments()
    elif command == 'heapsort':
        run_heapsort_experiments()
    elif command == 'pqueue':
        run_priority_queue_experiments()
    elif command == 'demo':
        run_demo()
    elif command == 'tests':
        sys.exit(0 if run_tests() else 1)
    else:
        print(__doc__)


if __name__ == "__main__":
    main()
