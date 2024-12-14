import json
import random

def generate_large_dataset(size, output_file):
    dataset = {
        "MovieID": list(range(1, size + 1)),
        "Title": [f"Movie {i} (1994)" for i in range(1, size + 1)],
        "Year": [random.choice([1994, 2006, 2010]) for _ in range(size)],
    }
    with open(output_file, "w") as f:
        json.dump(dataset, f, indent=4)

# Generate datasets
sizes = [100, 1000, 10000]
for size in sizes:
    generate_large_dataset(size, f"movies_{size}.json")
