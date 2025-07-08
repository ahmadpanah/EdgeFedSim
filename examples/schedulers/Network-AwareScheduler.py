from edgefedsim.schedulers.abstract_scheduler import AbstractScheduler

class NetworkAwareScheduler(AbstractScheduler):
    """
    Assigns tasks to the same cluster as their parent task if possible.
    Falls back to the least-loaded node otherwise.
    """
    def schedule(self, tasks, federation_state):
        placements = []
        all_nodes = [node for cluster in federation_state.clusters for node in cluster.nodes]

        if not all_nodes:
            return []

        for task in tasks:
            parent_task = task.dependencies[0] if task.dependencies else None
            local_cluster = None

            if parent_task and parent_task.host_node:
                # Find the cluster of the parent task's host node
                local_cluster = next(c for c in federation_state.clusters if parent_task.host_node in c.nodes)

            # Prioritize nodes in the local cluster
            target_nodes = local_cluster.nodes if local_cluster else all_nodes

            # Find the least loaded node in the target list
            # Note: The paper mentions checking for sufficient resources,
            # which is handled by the simulation engine after placement.
            best_node = max(target_nodes, key=lambda node: node.power_model.available_mips)
            placements.append((task, best_node))

        return placements```