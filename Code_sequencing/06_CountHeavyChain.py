import pandas as pd

# List of file paths for the 5 files
file_paths = [
    'output_heavy.csv',
    'output_light.csv',
]

# Process each file and count sequences without error messages
for file_path in file_paths:
    # Load the CSV file
    df = pd.read_csv(file_path)

    # Count rows where 'error_message' column is NaN (i.e., no error)
    sequences_without_error = df['error_message'].isna().sum()

    # Print the result for each file
    print(f"File: {file_path}")
    print(f"Number of sequences without error: {sequences_without_error}\n")