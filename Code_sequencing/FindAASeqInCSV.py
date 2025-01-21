import pandas as pd


# Specify the path to your CSV file
csv_file = '04_MCF7_uniqueAA.csv'
# Specify the sequence you're looking for
sequence = 'QITLKESGPTLVKPTQTLTLTCTFSGFSLSTTGVGLAWIRQPPGQALEWLALIYWDDDKHYSSSLRSRLTITKDTSKNQVVLTMTNMNPVDTGTYYCAHTSNDSDGLDAFDIWGQGTMVTVS'

# Function to find a sequence in the CSV file and return its corresponding count
def find_sequence_count(csv_file, sequence):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_file)

    # Filter the DataFrame for the specified sequence
    result = df[df['Amino Acid Sequence'].str.contains(sequence, na=False)]
    # Check if any sequences were found and return the corresponding counts
    if not result.empty:
        return result[['Amino Acid Sequence', 'Count']]  # Return matching sequences and their counts
    else:
        return None  # If no sequences are found

# Get the corresponding count for the sequence
count = find_sequence_count(csv_file, sequence)

# Output the result
if count is not None:
    print(f"The count for sequence {sequence} is: {count}")
else:
    print(f"Sequence {sequence} not found in the file.")
