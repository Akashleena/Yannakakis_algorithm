import json
import time
import matplotlib.pyplot as plt
from your_yannakakis_functions import apply_selection, downward_semi_join, upward_full_join

# Dataset sizes and execution times
dataset_sizes = [100, 1000, 10000]
execution_times = []

for size in dataset_sizes:
    file_name = f"movies_{size}.json"
    with open(file_name, "r") as f:
        movies = json.load(f)

    relations = {
        "R1": {"MovieID": list(map(int, movies["MovieID"])), "Title": movies["Title"]},
        "R2": {"MovieID": list(map(int, movies["MovieID"])), "Year": movies["Year"]},
    }
    join_tree = [("R1", "R2")]

    start_time = time.time()
    relations["R1"] = apply_selection(relations["R1"], lambda row: "1994" in row["Title"])
    relations = downward_semi_join(join_tree, relations)
    relations = upward_full_join(join_tree, relations)
    end_time = time.time()

    execution_times.append(end_time - start_time)

# Visualization with a logarithmic y-axis
plt.figure(figsize=(10, 6))
bars = plt.bar(dataset_sizes, execution_times, color='skyblue', edgecolor='black')
plt.yscale("log")  # Logarithmic scale for y-axis
plt.xlabel("Dataset Size (Number of Tuples)", fontsize=12)
plt.ylabel("Execution Time (Seconds) [Log Scale]", fontsize=12)
plt.title("Scalability Analysis of Yannakakis Algorithm", fontsize=14)

# Annotate bars with execution times
for bar, time in zip(bars, execution_times):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), f"{time:.2f}s",
             ha='center', va='bottom', fontsize=10)

plt.xticks(dataset_sizes, fontsize=10)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Save the plot
output_file = "scalability_analysis_log.png"
plt.savefig(output_file)
print(f"Plot saved as {output_file}")
plt.show()
