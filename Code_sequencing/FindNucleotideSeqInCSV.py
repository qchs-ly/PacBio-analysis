import pandas as pd

# Specify the path to your CSV file
csv_file = '02_MCF7_extract_sequences_count.csv'

# Specify the nucleotide sequence you're looking for
nucleotide_sequence = 'CAGGTACAGCTGCAGCAGTCAGGTCCAGGACTGGTGAAGCCCTCGCAGACCCTCTCACTCACCTGTGCCATCTCCGGTGACAGTGTCTCTAGCAACAGTGCTTCTTGGAACTGGGTCAGGCAGTCCCCATCGAGAGGCCTTGAGTGGCTGGGAAAGACATACTACAGGTCCAAATGGAATTATGATTTTGCAACTTCAATGAATGGTCGGGTCATCGTCACCCCCGACACATCCAAGAACCAGGTCTCCCTGCAGCTGAACTCTGTGACTCCCGAGGACACGGCTGTATATTACTGTGCAAGAGGGAGAGATAACGCTTTTGATATTTGGGGCCAAGGGACAATGGTCACCGTCTCTTCAGAATTC'

# Function to find sequences that contain the target sequence and return their counts
def find_containing_sequences(csv_file, nucleotide_sequence):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_file)

    # Filter the DataFrame for sequences that contain the target sequence
    result = df[df['Sequence'].str.contains(nucleotide_sequence, na=False)]

    # Check if any sequences were found and return the corresponding counts
    if not result.empty:
        return result[['Sequence', 'Count']]  # Return matching sequences and their counts
    else:
        return None  # If no sequences are found

# Get the sequences containing the nucleotide sequence and their counts
result = find_containing_sequences(csv_file, nucleotide_sequence)

# Output the result
if result is not None:
    print(f"Sequences containing the target sequence and their counts are:\n{result}")
else:
    print(f"No sequences containing the target sequence were found in the file.")
