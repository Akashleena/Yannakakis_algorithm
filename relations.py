relations = {
    "R1": {"A": [1, 2, 3], "B": ["x", "y", "z"]},
    "R2": {"B": ["x", "z"], "C": [10, 30]},
    "R3": {"A": [1, 3], "D": [100, 300]}
}

join_tree = [("R1", "R2"), ("R1", "R3")]

#Function to print relations
def print_relation(name, relation):
    print(f"Relation {name}:")
    for key in relation:
        print(f" {key}: {relation[key]}")
    print()

#Function to print join tree
def print_join_tree(tree):
    print("Join Tree:")
    for parent, child in tree:
        print(f" Parent: {parent}, Child: {child}")
    print()

#Function to apply selection on a relation
def apply_selection(relation, condition):
    """
    Filters a relation based on a given condition.
    
    Parameters:
    - relation(dict): The relation to filter, represented as a dictionary of columns.
    -condition(function): A function that takes a row (dict) and returns True if the row should be kept.
    
    Returns:
    -filtered_relation (dict): A new relation containing only the rows that satisfy the condition.
    """
    
    #Initialize an empty dictionary for the filtered relation
    filtered_relation = {key: [] for key in relation}
    
    #Iterate over each row (tuple of values across all columns)
    for i in range(len(next(iter(relation.values())))):  # Assumes all columns are the same length
        # Create a dictionary representing this row
        row = {key: relation[key][i] for key in relation}
        
        # Check the condition for this row
        if condition(row):
            # If the row satisfies the condition, add it to the filtered relation
            for key in relation:
                filtered_relation[key].append(row[key])

    return filtered_relation

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

# Main function
def main():
    # Print the original relations
    print("Original Relations:")
    for name, relation in relations.items():
        print_relation(name, relation)

    # Apply selection to R1
    print("Applying selection to R1 (A > 1):")
    relations["R1"] = apply_selection(relations["R1"], condition_R1)

    # Print the filtered relations
    print("Filtered Relations:")
    for name, relation in relations.items():
        print_relation(name, relation)

    # Print the join tree
    print_join_tree(join_tree)

if __name__ == "__main__":
    main()

