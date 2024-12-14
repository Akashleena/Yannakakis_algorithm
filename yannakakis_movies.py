import time
import json
import matplotlib.pyplot as plt
from your_yannakakis_functions import apply_selection, downward_semi_join, upward_full_join
from relations import print_relation, print_join_tree

def run_yannakakis_for_dataset(dataset_file):
    """
    Load dataset from file and run the Yannakakis algorithm.
    """
    # Load relations from JSON
    with open(dataset_file, "r") as f:
        relations = json.load(f)

    # Define the join tree
    join_tree = [("R1", "R2"), ("R1", "R3")]

    # Debug: Preview input data
    print(f"\nRunning Yannakakis on Dataset: {dataset_file}")
    print_relation("R1", relations["R1"])
    print_relation("R2", relations["R2"])
    print_relation("R3", relations["R3"])

    # Apply selection to R1
    print("\nApplying selection to R1 (filter movies after 2000):")
    relations["R1"] = apply_selection(relations["R1"], lambda row: row["Year"] > 2000)
    print_relation("R1", relations["R1"])

    # Downward semi-join computation
    print("\nPerforming downward semi-join computation:")
    start_semi_join = time.time()
    relations = downward_semi_join(join_tree, relations)
    end_semi_join = time.time()
    print(f"Downward Semi-Join Execution Time: {end_semi_join - start_semi_join:.2f} seconds")

    # Show intermediate relations after downward semi-join
    print("\nRelations after downward semi-join:")
    print_relation("R2", relations["R2"])
    print_relation("R3", relations["R3"])

    # Upward full join computation
    print("\nPerforming upward full join computation:")
    start_full_join = time.time()
    relations = upward_full_join(join_tree, relations)
    end_full_join = time.time()
    print(f"Upward Full Join Execution Time: {end_full_join - start_full_join:.2f} seconds")

    # Final relations after upward full join
    print("\nFinal Relations after upward full join:")
    print_relation("R1", relations["R1"])

    # Total execution time
    total_execution_time = (end_semi_join - start_semi_join) + (end_full_join - start_full_join)
    print(f"Total Execution Time for {dataset_file}: {total_execution_time:.2f} seconds\n")
    return total_execution_time

def plot_results(sizes, times):
    """
    Plot execution times for different dataset sizes on a logarithmic scale.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, times, marker="o", linestyle="-", color="blue")
    plt.xscale("log")  # Set x-axis to logarithmic scale
    plt.yscale("log")  # Set y-axis to logarithmic scale
    plt.xlabel("Dataset Size (Number of Tuples, Log Scale)", fontsize=12)
    plt.ylabel("Execution Time (Seconds, Log Scale)", fontsize=12)
    plt.title("Yannakakis Algorithm Performance (Log-Log Scale)", fontsize=14)
    plt.grid(True, which="both", linestyle="--", alpha=0.7)
    plt.savefig("yannakakis_performance_log.png")
    print("Performance plot saved as 'yannakakis_performance_log.png'")
    plt.show()


if __name__ == "__main__":
    sizes = [1000, 5000, 10000, 20000, 50000]
    results = {}
    execution_times = []
    
    for size in sizes:
        dataset_file = f"relations_{size}.json"
        time_taken = run_yannakakis_for_dataset(dataset_file)
        results[size] = time_taken
        execution_times.append(time_taken)

    # Print results summary
    print("\nSummary of Results:")
    for size, time_taken in results.items():
        print(f"Dataset Size: {size}, Total Execution Time: {time_taken:.2f} seconds")

    # Plot results
    plot_results(sizes, execution_times)
