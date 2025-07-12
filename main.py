# main.py

import simpy
import numpy as np
import random
from tabulate import tabulate

from edgefedsim.simulation import Simulation
from edgefedsim.scheduler import CerebrumScheduler, NetworkAwareHeuristicScheduler, FLBlockScheduler
from edgefedsim.utils import *

def run_experiment(scheduler_class, policy=None):
    random.seed(RANDOM_SEED)
    np.random.seed(RANDOM_SEED)
    env = simpy.Environment()
    sim = Simulation(env, scheduler_class, policy=policy)
    env.process(sim.run())  # <-- ADD THIS LINE
    env.run() 
    return sim.print_results()

if __name__ == "__main__":
    
    all_results = []

    # Run experiment for each scheduler
    all_results.append(run_experiment(NetworkAwareHeuristicScheduler))
    all_results.append(run_experiment(FLBlockScheduler))
    
    # Run experiments for different Cerebrum policies
    all_results.append(run_experiment(CerebrumScheduler, policy='balanced'))
    all_results.append(run_experiment(CerebrumScheduler, policy='performance'))
    all_results.append(run_experiment(CerebrumScheduler, policy='energy'))
    all_results.append(run_experiment(CerebrumScheduler, policy='cost'))

    # Print final summary table
    headers = ["Scheduler", "Avg Makespan (s)", "Avg Energy (kJ)", "Avg Cost ($)", "Avg Latency (ms)"]
    table_data = [
        [
            r['scheduler'],
            f"{r['makespan']:.2f}",
            f"{r['energy']:.2f}",
            f"${r['cost']:.2f}",
            f"{r['latency']:.2f}"
        ] for r in all_results
    ]

    print("\n\n--- Overall Comparison ---")
    print(tabulate(table_data, headers=headers, tablefmt="grid"))

# Ensure CSV is written only after all experiments are finished
import csv, os, sys
csv_path = os.path.abspath("results.csv")
try:
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(table_data)
    print(f"\nResults saved to {csv_path}")
except Exception as e:
    print(f"\nFailed to write results to CSV: {e}", file=sys.stderr)