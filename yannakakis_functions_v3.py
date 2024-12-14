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

def downward_semi_join(join_order, relations):
    """
    Applies the downward semi-join step and logs intermediate relation sizes.
    """
    for parent, child in zip(join_order[:-1], join_order[1:]):
        join_attributes = list(set(relations[parent].keys()) & set(relations[child].keys()))
        print(f"\n--- Downward Semi-Join: {parent} -> {child} ---")
        print(f"Join Attributes: {join_attributes}")
        
        # Log size before semi-join
        child_size_before = len(relations[child][join_attributes[0]])
        print(f"Size of {child} before semi-join: {child_size_before}")

        # Perform semi-join
        relations[child] = semi_join(relations[parent], relations[child], join_attributes)
        
        # Log size after semi-join
        child_size_after = len(relations[child][join_attributes[0]])
        print(f"Size of {child} after semi-join: {child_size_after}")
        print(f"Tuples eliminated: {child_size_before - child_size_after}")

    return relations

def full_join(parent_relation, child_relation, join_attributes):
    """
    Performs a full join between parent and child relations.
    """
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

def upward_full_join(join_order, relations):
    """
    Applies the upward full join step in the reverse join order.
    """
    for parent, child in reversed(list(zip(join_order[:-1], join_order[1:]))):
        join_attributes = list(set(relations[parent].keys()) & set(relations[child].keys()))
        relations[parent] = full_join(relations[parent], relations[child], join_attributes)
    return relations
