# **CSE214 Project: Yannakakis Algorithm**

This project implements and evaluates the Yannakakis algorithm for query optimization on relational databases and test the order of joins.
Download dataset from [tp.fu-berlin.de](https://ftp.fu-berlin.de/pub/misc/movies/database/frozendata/)

### `requirements.txt`
- A list of Python dependencies required to run the project.
- Install these dependencies using:
  ```bash
  pip3 install -r requirements.txt

## Contents of yannakakis_project.zip
## **Python Scripts**

### `relations.py`
- A baseline implementation of the Yannakakis algorithm with synthetic relations and a simple join tree.
- Includes utility functions such as `print_relation` and `print_join_tree` for debugging and visualization.

### `load_parsed_data.py`
- Loads the parsed movies dataset (`parsed_movies.json`) into memory.
- Includes functionality to preview a small portion of the data for verification.

### `parse_movielist.py`
- Parses the raw `movies.list` file into a structured JSON file (`parsed_movies.json`).
- Helps transform unstructured data into a usable format for further analysis.

### `yannakakis_movies.py`
- Orchestrates the Yannakakis algorithm on the movies dataset.
- Implements the three key phases of the Yannakakis algorithm:
  1. **Selection**: Filters rows based on specified conditions.
  2. **Downward Semi-Join**: Removes dangling tuples.
  3. **Upward Full-Join**: Constructs the final join result.

### `your_yannakakis_functions.py`
- Contains the core functionality for the Yannakakis algorithm.
- Implements the `downward_semi_join` and `upward_full_join` steps.

### `eval_semijoin.py`
- Evaluates the performance of different semi-join order strategies.
- Tests strategies such as:
  - Random order
  - Left-to-right order
  - Heuristic-based order
- Provides insights into how the order of operations affects efficiency.

### `scalability_analysis.py`
- Tests the scalability of the Yannakakis algorithm with datasets of increasing sizes.
- Measures execution time and visualizes the results on a logarithmic scale for better interpretability.

### `convert_json_to_csv.py`
- Converts JSON files into CSV format for easier processing and compatibility with other tools.

### `generate_datasets.py`
- Generates synthetic datasets for testing the Yannakakis algorithm.
- Configurable to create datasets of varying sizes and attributes.

### `generate_generes.py`
- Creates a deterministic mapping of genres for the movies dataset.
- Ensures consistency across different test runs.

### `generate_years.py`
- Generates and assigns release years to movies in the dataset.
- Helps simulate realistic data for performance evaluation.

### `test_ipdata.py`
- Contains unit tests and debugging utilities for validating the implementation of the algorithm.

### `tabdata.py`
- Handles table-related data operations for the relations used in the Yannakakis algorithm.
- Provides helper functions for manipulating and querying tabular data.

### `yannakakis_functions_v2.py`
- An updated version of the core Yannakakis functions, improving upon the original implementation.
- Introduces optimizations and additional features for semi-joins and full-joins.

### `yannakakis_functions_v3.py`
- A further refined version of the Yannakakis functions with enhanced performance and scalability.
- Includes new strategies for evaluating join order performance.

### `yannakakis_join_orders.py`
- Implements and tests different join orders for the Yannakakis algorithm.
- Evaluates the impact of join orders on algorithm performance.

### `yannakakis_join_orders_v3.py`
- An advanced version of `yannakakis_join_orders.py` with improved heuristics for join order selection.
- Provides better execution time analysis and performance tuning.

## **Data Files**

### `parsed_movies.json`
- The parsed and structured version of the raw `movies.list` file.
- Used as the primary dataset for applying the Yannakakis algorithm.

### `relations_*.json`
- Synthetic relational datasets generated for testing the algorithm.
- Examples include `relations_1000.json`, `relations_5000.json`, and `relations_20000.json`.

### `relations_*_R[1-3].csv`
- CSV representations of individual relations (e.g., `relations_1000_R1.csv`).
- Facilitates external analysis and integration with tools like PostgreSQL.

### `movies_*.json`
- Subsets of the parsed movies dataset (e.g., `movies_1000.json`, `movies_10000.json`).
- Useful for testing on smaller datasets.

## **Visualization and Analysis**

### `yannakakis_join_order_performance.png`
- A performance visualization of different semi-join order strategies.
- Highlights the execution times of various approaches.

### `yannakakis_join_order_performance_v3.png`
- An updated visualization of semi-join performance using advanced strategies.
- Includes insights from `yannakakis_join_orders_v3.py`.

### `yannakakis_performance_log.png`
- A log-scale plot showing the scalability and performance of the Yannakakis algorithm.
- Visualizes execution time comparisons for various dataset sizes.





---
