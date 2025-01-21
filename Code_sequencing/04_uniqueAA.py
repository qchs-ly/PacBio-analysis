import pandas as pd

# List of input and output file pairs
file_pairs = [
    ('03_MCF7_AA.csv', '04_MCF7_uniqueAA.csv'),
    ('03_MCF10A_AA.csv', '04_MCF10A_uniqueAA.csv')
]

# Process each file pair
for input_file, output_file in file_pairs:
    # Load the input CSV file
    df = pd.read_csv(input_file)

    # Group by the 'Amino Acid Sequence' column and sum the counts in 'Amino Acid Count'
    df_grouped = df.groupby('Amino Acid Sequence').agg({'Count': 'sum'}).reset_index()

    # Save the grouped data to the output CSV file
    df_grouped.to_csv(output_file, index=False)

    # Print a message to confirm processing
    print(f"Processed {input_file} and saved results to {output_file}")