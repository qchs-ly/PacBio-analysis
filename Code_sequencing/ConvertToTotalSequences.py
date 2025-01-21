#My dataset has two format: the first one is unique sequences and their count. the second one is all the sequences
#the first one is csv file. How to convert the first file into a csv file of the second format
import pandas as pd


import pandas as pd

# Load the two CSV files containing unique sequences and their counts
csv_file1 = '04_MCF7_uniqueAA.csv'  # Replace with your first file path
csv_file2 = '04_MCF10A_uniqueAA.csv'  # Replace with your second file path
output_file1 = '04_MCF7_Total.csv'
output_file2 = '04_MCF10A_Total.csv'

# Specify the column names (adjust according to your CSV structure)
sequence_column = 'Amino Acid Sequence'  # Column containing unique sequences
count_column = 'Count'  # Column containing the count for each sequence

# Function to expand sequences based on their count and save to a new CSV
def expand_sequences(csv_file, output_file):
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(csv_file)

    # Repeat each sequence according to its count
    expanded_sequences = df.loc[df.index.repeat(df[count_column])][sequence_column]

    # Save the expanded sequences to a new CSV file
    expanded_sequences.to_csv(output_file, index=False, header=False)
    print(f"Conversion complete! The sequences have been expanded and saved to '{output_file}'.")


# Expand sequences for the first CSV file and save to a separate output file
expand_sequences(csv_file1, output_file1)

# Expand sequences for the second CSV file and save to a separate output file
expand_sequences(csv_file2, output_file2)
