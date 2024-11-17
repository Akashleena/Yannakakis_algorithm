# Define relations and join tree
relations = {
    "R1": {"A": [1, 2, 3], "B": ["x", "y", "z"]},
    "R2": {"B": ["x", "z"], "C": [10, 30]},
    "R3": {"A": [1, 3], "D": [100, 300]}
}

join_tree = [("R1", "R2"), ("R1", "R3")]

# Function to print a relation
def print_relation(name, relation):
    """
    Prints the content of a relation in a readable format.

    Parameters:
    - name (str): The name of the relation.
    - relation (dict): The relation to print, represented as a dictionary of columns.
    """
    print(f"Relation {name}:")
    for key in relation:
        print(f"  {key}: {relation[key]}")
    print()

# Function to print the join tree
def print_join_tree(tree):
    """
    Prints the join tree in a readable format.

    Parameters:
    - tree (list of tuples): The join tree, where each tuple represents a parent-child pair.
    """
    print("Join Tree:")
    for parent, child in tree:
        print(f"  Parent: {parent}, Child: {child}")
    print()

# Function to apply selection on a relation
def apply_selection(relation, condition):
    """
    Filters a relation based on a given condition.

    Parameters:
    - relation (dict): The relation to filter, represented as a dictionary of columns.
    - condition (function): A function that takes a row (dict) and returns True if the row should be kept.

    Returns:
    - filtered_relation (dict): A new relation containing only the rows that satisfy the condition.
    """
    filtered_relation = {key: [] for key in relation}

    # Iterate over each row (tuple of values across all columns)
    for i in range(len(next(iter(relation.values())))):  # Assumes all columns are the same length
        row = {key: relation[key][i] for key in relation}  # Create a dictionary for this row
        if condition(row):  # Check the condition
            for key in relation:
                filtered_relation[key].append(row[key])

    return filtered_relation

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

# Function to perform downward semi-join computation
def downward_semi_join(join_tree, relations):
    """
    Performs the downward semi-join computation for all parent-child pairs in the join tree.

    Parameters:
    - join_tree (list of tuples): The join tree, where each tuple is (parent, child).
    - relations (dict): Dictionary of relations.

    Returns:
    - Updated relations dictionary with filtered child relations.
    """
    for parent, child in join_tree:
        join_attributes = list(set(relations[parent].keys()) & set(relations[child].keys()))
        relations[child] = semi_join(relations[parent], relations[child], join_attributes)
    return relations

# Example selection condition: Filter R1 to keep only rows where A > 1
def condition_R1(row):
    """
    Selection criterion for R1: Keep rows where A > 1.

    Parameters:
    - row (dict): A dictionary representing a row from the relation.

    Returns:
    - bool: True if the row satisfies the condition, False otherwise.
    """
    return row["A"] > 1

def main(relations):
    # Print the original relations
    print("Original Relations:")
    for name, relation in relations.items():
        print_relation(name, relation)

    # Apply selection to R1
    print("Applying selection to R1 (A > 1):")
    relations["R1"] = apply_selection(relations["R1"], condition_R1)

    # Perform downward semi-join computation
    print("Performing downward semi-join computation:")
    relations = downward_semi_join(join_tree, relations)

    # Print the updated relations
    print("Relations after downward semi-join:")
    for name, relation in relations.items():
        print_relation(name, relation)

    # Print the join tree
    print_join_tree(join_tree)

if __name__ == "__main__":
    main(relations)
