def apply_selection(relation, condition):
    """
    Filters rows in a relation based on a condition.
    """
    filtered_relation = {key: [] for key in relation}
    for i in range(len(relation[next(iter(relation.keys()))])):
        row = {key: relation[key][i] for key in relation}
        if condition(row):
            for key in relation:
                filtered_relation[key].append(row[key])
    return filtered_relation

def semi_join(parent_relation, child_relation, join_attributes):
    """
    Performs a semi-join between parent and child relations.
    """
    if not join_attributes:
        print("No join attributes found between parent and child.")
        return child_relation

    # Debug: Print relation keys and join attributes
    print(f"Parent Relation Keys: {list(parent_relation.keys())}")
    print(f"Child Relation Keys: {list(child_relation.keys())}")
    print(f"Join Attributes: {join_attributes}")

    parent_tuples = set(
        tuple(parent_relation[attr][i] for attr in join_attributes)
        for i in range(len(parent_relation[join_attributes[0]]))
    )
    filtered_child_relation = {key: [] for key in child_relation}
    for i in range(len(child_relation[join_attributes[0]])):
        child_tuple = tuple(child_relation[attr][i] for attr in join_attributes)
        if child_tuple in parent_tuples:
            for key in child_relation:
                filtered_child_relation[key].append(child_relation[key][i])
    return filtered_child_relation

def downward_semi_join(join_tree, relations):
    """
    Applies the downward semi-join step.
    """
    for parent, child in join_tree:
        join_attributes = list(set(relations[parent].keys()) & set(relations[child].keys()))
        if join_attributes:  # Debug only if there are common attributes
            print(f"Join Attributes for {parent} and {child}: {join_attributes}")
        relations[child] = semi_join(relations[parent], relations[child], join_attributes)
    return relations

def full_join(parent_relation, child_relation, join_attributes):
    """
    Performs a full join between parent and child relations.
    """
    if not join_attributes:
        # If no common join attributes, return the parent relation unchanged
        print("No join attributes found between parent and child for full join.")
        return parent_relation

    updated_parent_relation = {key: [] for key in parent_relation}
    for key in child_relation:
        if key not in updated_parent_relation:
            updated_parent_relation[key] = []

    for i in range(len(parent_relation[join_attributes[0]])):
        parent_row = {key: parent_relation[key][i] for key in parent_relation}
        match_found = False
        for j in range(len(child_relation[join_attributes[0]])):
            child_row = {key: child_relation[key][j] for key in child_relation}
            if all(parent_row[attr] == child_row[attr] for attr in join_attributes):
                match_found = True
                for key in updated_parent_relation:
                    updated_parent_relation[key].append(
                        child_row.get(key, parent_row.get(key))
                    )
                break
        if not match_found:
            for key in parent_relation:
                updated_parent_relation[key].append(parent_row[key])
            for key in child_relation:
                if key not in parent_relation:
                    updated_parent_relation[key].append(None)
    return updated_parent_relation

def upward_full_join(join_tree, relations):
    """
    Applies the upward full join step.
    """
    for parent, child in reversed(join_tree):
        join_attributes = list(set(relations[parent].keys()) & set(relations[child].keys()))
        if join_attributes:  # Debug only if there are common attributes
            print(f"Upward Join Attributes for {parent} and {child}: {join_attributes}")
        relations[parent] = full_join(relations[parent], relations[child], join_attributes)
    return relations

