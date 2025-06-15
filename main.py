# main.py

import simpy
import numpy as np
import random
from tabulate import tabulate

from simulation import Simulation
from scheduler import CerebrumScheduler, NetworkAwareHeuristicScheduler, FLBlockScheduler
from utils import *

def run_experiment(scheduler_class, policy=None):
    """Runs a single simulation experiment for a given scheduler."""
    random.seed(RANDOM_SEED)
    np.random.seed(RANDOM_SEED)
    
    env = simpy.Environment()
    sim = Simulation(env, scheduler_class, policy=policy)
    env.run() # The simulation runs until all generated workflows are processed
    
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