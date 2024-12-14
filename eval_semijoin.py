import time
import random

# Example relations
relations = {
    "R1": {"A": [1, 2, 3], "B": ["x", "y", "z"]},
    "R2": {"B": ["x", "z"], "C": [10, 30]},
    "R3": {"A": [1, 3], "D": [100, 300]}
}

# Example join tree
join_tree = [("R1", "R2"), ("R1", "R3")]

# Relation sizes (for heuristic-based strategy)
relation_sizes = {
    "R1": len(relations["R1"]["A"]),
    "R2": len(relations["R2"]["B"]),
    "R3": len(relations["R3"]["A"])
}

# Function to perform a semi-join
def semi_join(parent_relation, child_relation, join_attributes):
    """
    Performs a semi-join between a parent and a child relation.

    Parameters:
    - parent_relation (dict): The parent relation.
    - child_relation (dict): The child relation.
    - join_attributes (list): The attributes to join on.

    Returns:
    - filtered_child_relation (dict): The child relation with tuples that match the parent relation.
    """
    parent_tuples = set(
        tuple(parent_relation[attr][i] for attr in join_attributes)
        for i in range(len(next(iter(parent_relation.values()))))
    )

    filtered_child_relation = {key: [] for key in child_relation}
    for i in range(len(next(iter(child_relation.values())))):
        child_tuple = tuple(child_relation[attr][i] for attr in join_attributes)
        if child_tuple in parent_tuples:
            for key in child_relation:
                filtered_child_relation[key].append(child_relation[key][i])

    return filtered_child_relation

# Function to evaluate semi-join order
def evaluate_semi_join_order(join_tree, relations, order):
    """
    Evaluates the performance of a given semi-join order.

    Parameters:
    - join_tree (list of tuples): The join tree.
    - relations (dict): Dictionary of relations.
    - order (list): The order of semi-joins to perform.

    Returns:
    - Execution time in seconds.
    """
    start_time = time.time()
    for parent, child in order:
        join_attributes = list(set(relations[parent].keys()) & set(relations[child].keys()))
        relations[child] = semi_join(relations[parent], relations[child], join_attributes)
    return time.time() - start_time

# Define different strategies for semi-join orders
orders = []

# 1. Random Order
random_order = random.sample(join_tree, len(join_tree))
orders.append(("Random Order", random_order))

# 2. Left-to-Right Order (Default)
left_to_right_order = [("R1", "R2"), ("R1", "R3")]
orders.append(("Left-to-Right Order", left_to_right_order))

# 3. Heuristic-Based Order (Relation Size)
heuristic_order = sorted(join_tree, key=lambda x: relation_sizes[x[1]])
orders.append(("Heuristic-Based Order", heuristic_order))

# Test each strategy
results = {}
for strategy_name, order in orders:
    # Reset relations for each test
    test_relations = {
        "R1": {"A": [1, 2, 3], "B": ["x", "y", "z"]},
        "R2": {"B": ["x", "z"], "C": [10, 30]},
        "R3": {"A": [1, 3], "D": [100, 300]}
    }
    execution_time = evaluate_semi_join_order(join_tree, test_relations, order)
    results[strategy_name] = execution_time

# Print results
print("Semi-Join Order Performance:")
for strategy, time_taken in results.items():
    print(f"{strategy}: {time_taken:.6f} seconds")
