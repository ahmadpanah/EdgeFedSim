# utils.py

# --- SIMULATION PARAMETERS ---
RANDOM_SEED = 42
SIM_DURATION = 10000  # Simulation time in seconds
WORKFLOW_ARRIVAL_RATE = 15 # New workflow every X seconds on average

# --- INFRASTRUCTURE PARAMETERS ---
# Power consumption model: P(util) = P_idle + (P_max - P_idle) * util
POWER_IDLE_CPU = 100  # Watts
POWER_MAX_CPU = 250   # Watts

# Node types [CPU (cores), Memory (GB)]
NODE_CONFIGS = {
    "small_edge": [4, 8],
    "medium_edge": [8, 16],
    "large_cloud": [32, 128]
}

# Cluster types and their node composition
CLUSTER_CONFIGS = {
    "Retail_Edge": {"type": "small_edge", "count": 5},
    "Factory_Floor": {"type": "medium_edge", "count": 10},
    "Cloud": {"type": "large_cloud", "count": 20}
}

# Network characteristics (Latency in ms, Bandwidth in Mbps)
NETWORK_LATENCY_INTRA_CLUSTER = 1
NETWORK_BANDWIDTH_INTRA_CLUSTER = 1000  # 1 Gbps

NETWORK_LATENCY_INTER_CLUSTER = 50
NETWORK_BANDWIDTH_INTER_CLUSTER = 100   # 100 Mbps

# Cost model ($/hour)
CLOUD_NODE_COST_PER_HOUR = 0.20
EDGE_NODE_COST_PER_HOUR = 0.0  # Assume edge nodes are a sunk cost

# --- WORKFLOW PARAMETERS ---
NUM_WORKFLOWS = 200
MIN_TASKS = 20
MAX_TASKS = 100

# Task resource requirements
TASK_CPU_REQ_RANGE = (0.5, 2.0)  # cores
TASK_MEM_REQ_RANGE = (0.5, 2.0)  # GB
TASK_BASE_RUNTIME_RANGE = (5, 20) # seconds
TASK_DATA_SIZE_RANGE = (10, 500) # MB (megabytes)
CONTAINER_IMAGE_SIZE = 200 # MB

# --- SCHEDULER PARAMETERS ---
# For Cerebrum
PREDICTION_HORIZON = 60 # seconds into the future
CEREBRUM_POLICY_WEIGHTS = {
    'performance': {'w_perf': 1.0, 'w_energy': 0.0, 'w_cost': 0.0},
    'energy':      {'w_perf': 0.0, 'w_energy': 1.0, 'w_cost': 0.0},
    'cost':        {'w_perf': 0.0, 'w_energy': 0.0, 'w_cost': 1.0},
    'balanced':    {'w_perf': 0.4, 'w_energy': 0.3, 'w_cost': 0.3},
}

# For Baseline Schedulers
FL_BLOCK_LATENCY = 0.5 # 500ms consensus latency