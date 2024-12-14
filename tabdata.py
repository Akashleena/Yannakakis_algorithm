
import pandas as pd

# Define the tabular data for Yannakakis Join Order Performance
data = {
    "Dataset Size": [1000, 5000, 10000, 20000],
    "R1 -> R2 -> R3": [0.01, 0.20, 0.60, 1.94],
    "R1 -> R3 -> R2": [0.32, 7.82, 29.58, 119.39],
    "R3 -> R1 -> R2": [0.31, 7.53, 29.96, 119.39],
    "R2 -> R1 -> R3": [0.02, 0.28, 1.22, 3.98],
    "R3 -> R2 -> R1": [0.40, 9.74, 38.92, 154.93],
}

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Display the DataFrame to the user
import ace_tools as tools; tools.display_dataframe_to_user(name="Yannakakis Join Order Performance Results", dataframe=df)

