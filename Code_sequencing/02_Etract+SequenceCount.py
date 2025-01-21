from Bio import SeqIO
import csv
from collections import defaultdict


# Example usage for MCF7 and MCF10A
input_fasta_mcf7 = "01_Combined_MCF7.fasta"
input_fasta_mcf10a = "01_Combined_MCF10A.fasta"

output_csv_mcf7 = "02_MCF7_extract_sequences_count.csv"
output_csv_mcf10a = "02_MCF10A_extract_sequences_count.csv"

# Define the left and right motifs
left_motif = "CTCTGCAGGCTAGTGGTGGTGGTGGTTCTGGTGGTGGTGGTTCTGGTGGTGGTGGTTCTGCTAGC"
right_motif = "TCCGGAATTCTA"


# Function to extract the region between the left and right motifs
def extract_region(sequence, left, right):
    start = sequence.find(left)
    end = sequence.find(right, start + len(left))

    if start != -1 and end != -1:
        return sequence[start + len(left):end]  # Extract the region between
    return None  # If not found, return None


# Function to process a FASTA file and count unique sequences
def process_fasta(input_fasta, left_motif, right_motif):
    sequence_counts = defaultdict(int)

    # Parse the input FASTA file
    for record in SeqIO.parse(input_fasta, "fasta"):
        sequence = str(record.seq)
        # Extract the region between the motifs
        extracted_region = extract_region(sequence, left_motif, right_motif)
        if extracted_region:
            sequence_counts[extracted_region] += 1  # Count the extracted region

    return sequence_counts


# Function to write the results to a CSV file
def write_to_csv(sequence_counts, output_csv):
    with open(output_csv, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Sequence", "Count"])
        for seq, count in sequence_counts.items():
            writer.writerow([seq, count])


# Main function
def main(input_fasta, output_csv):
    sequence_counts = process_fasta(input_fasta, left_motif, right_motif)
    write_to_csv(sequence_counts, output_csv)



# Process both files and save the output
main(input_fasta_mcf7, output_csv_mcf7)
main(input_fasta_mcf10a, output_csv_mcf10a)