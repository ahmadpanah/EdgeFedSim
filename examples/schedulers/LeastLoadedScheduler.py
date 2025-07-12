
from edgefedsim.schedulers.abstract_scheduler import AbstractScheduler

class LeastLoadedScheduler(AbstractScheduler):
    """
    Assigns each task to the node with the highest available CPU capacity.
    """
    def schedule(self, tasks, federation_state):
        placements = []
        all_nodes = [node for cluster in federation_state.clusters for node in cluster.nodes]

        if not all_nodes:
            return []

        for task in tasks:
            # Find the node with the maximum available MIPS
            best_node = max(all_nodes, key=lambda node: node.power_model.available_mips)
            placements.append((task, best_node))

        return placements