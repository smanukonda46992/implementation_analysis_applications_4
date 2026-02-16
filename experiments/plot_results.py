"""
Generate Plots for Heapsort Analysis

Reads timing data and generates comparison plots.
"""

import sys
from pathlib import Path
import csv

sys.path.insert(0, str(Path(__file__).parent.parent))

try:
    import matplotlib.pyplot as plt
    HAS_MATPLOTLIB = True
except ImportError:
    HAS_MATPLOTLIB = False


def load_results():
    """Load timing results from CSV."""
    data_file = Path(__file__).parent.parent / 'results' / 'raw_data' / 'heapsort_timings.csv'
    
    if not data_file.exists():
        print("No data file found. Run experiments first.")
        return None
    
    results = {}
    with open(data_file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            dist = row['distribution']
            algo = row['algorithm']
            size = int(row['size'])
            time = float(row['mean_time'])
            
            if dist not in results:
                results[dist] = {}
            if algo not in results[dist]:
                results[dist][algo] = {'sizes': [], 'times': []}
            
            results[dist][algo]['sizes'].append(size)
            results[dist][algo]['times'].append(time)
    
    return results


def generate_plots(results):
    """Generate comparison plots."""
    if not HAS_MATPLOTLIB:
        print("matplotlib not installed. Skipping plots.")
        return
    
    output_dir = Path(__file__).parent.parent / 'results' / 'plots'
    output_dir.mkdir(parents=True, exist_ok=True)
    
    for dist, algos in results.items():
        plt.figure(figsize=(8, 5))
        for algo, data in algos.items():
            plt.plot(data['sizes'], data['times'], marker='o', label=algo)
        
        plt.title(f'Sorting Time vs Size ({dist})')
        plt.xlabel('Array Size')
        plt.ylabel('Time (seconds)')
        plt.legend()
        plt.grid(True)
        
        plt.savefig(output_dir / f'heapsort_{dist}.png')
        print(f"Saved: results/plots/heapsort_{dist}.png")
        plt.close()


def main():
    """Generate all plots."""
    print("Generating plots...")
    results = load_results()
    if results:
        generate_plots(results)
        print("Done!")


if __name__ == "__main__":
    main()
