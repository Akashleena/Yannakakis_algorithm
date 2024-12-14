import time
import json
import matplotlib.pyplot as plt
from yannakakis_functions_v2 import apply_selection, downward_semi_join, upward_full_join
from relations import print_relation

def run_yannakakis_with_order(dataset_file, join_order):
    """
    Load dataset from file and run the Yannakakis algorithm for a specific join order.
    """
    with open(dataset_file, "r") as f:
        relations = json.load(f)

    # Debug: Display join order
    print(f"\nTesting Join Order: {' -> '.join(join_order)}")

    # Apply selection to R1
    relations["R1"] = apply_selection(relations["R1"], lambda row: row["Year"] > 2000)

    # Downward semi-join computation
    start_semi_join = time.time()
    relations = downward_semi_join(join_order, relations)
    end_semi_join = time.time()

    # Upward full join computation
    start_full_join = time.time()
    relations = upward_full_join(join_order, relations)
    end_full_join = time.time()

    # Calculate total execution time
    total_execution_time = (end_semi_join - start_semi_join) + (end_full_join - start_full_join)
    return total_execution_time

def plot_results(results):
    """
    Plot execution times for different join orders.
    """
    plt.figure(figsize=(12, 8))
    for order, times in results.items():
        sizes = list(times.keys())
        exec_times = list(times.values())
        plt.plot(sizes, exec_times, marker="o", label=f"Join Order: {order}")

    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel("Dataset Size (Number of Tuples, Log Scale)", fontsize=12)
    plt.ylabel("Execution Time (Seconds, Log Scale)", fontsize=12)
    plt.title("Yannakakis Algorithm Performance Across Join Orders", fontsize=14)
    plt.legend(fontsize=10)
    plt.grid(True, which="both", linestyle="--", alpha=0.7)
    plt.savefig("yannakakis_join_order_performance.png")
    print("Performance plot saved as 'yannakakis_join_order_performance.png'")
    plt.show()

if __name__ == "__main__":
    sizes = [1000, 5000, 10000, 20000]
    join_orders = [
        ["R1", "R2", "R3"],  # Default order
        ["R1", "R3", "R2"],  # Alternative order 1
        ["R3", "R1", "R2"],  # Alternative order 2
        ["R2", "R1", "R3"],  # Alternative order 3
        ["R3", "R2", "R1"],  # Alternative order 4 (new)
    ]

    results = { " -> ".join(order): {} for order in join_orders }

    for size in sizes:
        dataset_file = f"relations_{size}.json"
        for join_order in join_orders:
            order_name = " -> ".join(join_order)
            time_taken = run_yannakakis_with_order(dataset_file, join_order)
            results[order_name][size] = time_taken
            print(f"Size: {size}, Join Order: {order_name}, Time: {time_taken:.2f} seconds")

    # Plot results
    plot_results(results)
