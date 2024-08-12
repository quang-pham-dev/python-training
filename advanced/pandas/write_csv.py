import os
import pandas as pd  # alias pd

# Write to csv from data.csv with df.head().to_string()import pandas as pd

# Read the data from data.csv into a DataFrame
file_path_input = os.path.join("advanced", "pandas", "data.csv")
file_path_output = os.path.join("advanced", "pandas", "output.csv")
try:
    df = pd.read_csv(file_path_input)
except FileNotFoundError:
    print("Error: The file was not found.")


# Write the first few rows of the DataFrame to a csv file
try:
    df.head().to_csv(file_path_output, index=False)
except Exception as e:
    print("Error: An unexpected error occurred.")
    # Log the error message for further investigation
    print(str(e))
