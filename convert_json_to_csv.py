import json
import csv

def json_to_csv(json_file, output_prefix):
    """
    Converts a JSON file containing R1, R2, R3 relations to separate CSV files.
    
    Parameters:
        json_file (str): Path to the input JSON file.
        output_prefix (str): Prefix for the output CSV files (e.g., "relations_1000").
    """
    with open(json_file, "r") as jf:
        data = json.load(jf)
    
    for relation_name, relation_data in data.items():
        output_file = f"{output_prefix}_{relation_name}.csv"
        keys = relation_data.keys()
        
        # Write to CSV
        with open(output_file, "w", newline="") as csv_file:
            writer = csv.writer(csv_file)
            # Write header
            writer.writerow(keys)
            # Write rows
            rows = zip(*[relation_data[key] for key in keys])
            writer.writerows(rows)
        
        print(f"Generated: {output_file}")


# Main script
if __name__ == "__main__":
    datasets = ["relations_1000.json", "relations_5000.json", "relations_10000.json", "relations_20000.json"]
    
    for dataset in datasets:
        prefix = dataset.split(".")[0]  # Extract the prefix (e.g., "relations_1000")
        json_to_csv(dataset, prefix)
