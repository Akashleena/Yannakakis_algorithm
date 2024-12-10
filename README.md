# Yannakakis_algorithm
cse214 project
relations.py:

A baseline implementation of the Yannakakis algorithm with synthetic relations and a simple join tree.
Includes utility functions like print_relation and print_join_tree.
load_parsed_data.py:

Loads the parsed movies dataset (parsed_movies.json).
Previews a small portion of the data for verification.
parse_movielist.py:

Parses the raw movies.list file into a structured JSON file (parsed_movies.json).
yannakakis_movies.py:

Orchestrates the Yannakakis algorithm on the movies dataset.
Implements selection, downward semi-join, and upward full-join phases.
your_yannakakis_functions.py:

Core functionality for selection, semi-join, and full-join.
Implements downward_semi_join and upward_full_join steps.
eval_semijoin.py:

Evaluates the performance of different semi-join orders.
Tests strategies like random order, left-to-right, and heuristic-based.
scalability_analysis.py:

Tests the scalability of the Yannakakis algorithm with increasing dataset sizes.
Visualizes execution time on a logarithmic scale.
