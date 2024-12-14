# Debugging Input Data: Check the content of R1, R2, and R3

# Load relations from relations.json
import json

with open("relations.json", "r") as f:
    relations = json.load(f)

# Function to preview relation data
def preview_relation(relation_name, relation_data):
    """
    Prints a preview of a relation's data.

    Parameters:
    - relation_name (str): Name of the relation.
    - relation_data (dict): Data of the relation.
    """
    print(f"\nPreview of {relation_name}:")
    if not relation_data:
        print(f"{relation_name} is empty!")
        return
    for key in relation_data:
        print(f"  {key}: {relation_data[key][:5]}")  # Print the first 5 rows

# Preview each relation
print("Validating Input Data:")
preview_relation("R1", relations["R1"])
preview_relation("R2", relations["R2"])
preview_relation("R3", relations["R3"])
