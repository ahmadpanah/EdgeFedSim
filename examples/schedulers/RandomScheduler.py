import random

class RandomScheduler(AbstractScheduler):
    """
    Schedules tasks to a random node in the federation.
    """
    def schedule(self, current_time, ready_tasks, federation_state):
        placements = []
        all_nodes = list(federation_state.nodes.values())

        for task in ready_tasks:
            # Filter nodes that meet the task's resource requirements
            suitable_nodes = [
                node for node in all_nodes
                if node.resources["cpu_mips"] >= task.requirements["cpu_mips"] and
                   node.resources["memory_mb"] >= task.requirements["memory_mb"]
            ]

            if suitable_nodes:
                # Select a random node from the suitable ones
                selected_node = random.choice(suitable_nodes)
                placements.append((task, selected_node))
            else:
                # Handle the case where no suitable node is found
                print(f"Warning: No suitable node found for task {task.id}")

        return placements