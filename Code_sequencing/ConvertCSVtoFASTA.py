import pandas as pd

file_pairs = [
    ('output_MCF7.csv', 'model_MCF7.fasta')
]

for input_file, output_file in file_pairs:
    # Load the CSV file
    df = pd.read_csv(input_file)

    # Open the output FASTA file for writing
    with open(output_file, 'w') as fasta_file:
        # Initialize a counter for sequence numbering
        seq_counter = 1

        # Iterate over each row in the DataFrame
        for _, row in df.iterrows():
            # Create the header using the counter (since no count column exists)
            fasta_header = f">seq{seq_counter}"

            # Write the header and sequence to the FASTA file
            fasta_file.write(f"{fasta_header}\n{row['Generated Sequence']}\n")

            # Increment the counter for the next sequence
            seq_counter += 1

    print(f"FASTA file written to {output_file}")
