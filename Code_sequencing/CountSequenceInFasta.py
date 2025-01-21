# check whether the target sequence is in a fasta file
# count the number of target sequence in fasta file
from Bio import SeqIO

# Define your target sequence
target_sequence = "GCTAGCAGAACCACCACCACCAGAACCACCACCACCAGAACCACCACCACCACTAGCCTGCAGAG"

# Define the path to your FASTA file
fasta_file = "/Volumes/DanMac/1_research/WangLab/02_DataStorage/MacminiPycharmFile/PacBioTry2/sequences.fasta"

# Initialize a counter for the target sequence occurrences
count = 0

# Parse the FASTA file and check each sequence
for record in SeqIO.parse(fasta_file, "fasta"):
    # Check if the target sequence is present in the current record's sequence
    if target_sequence in str(record.seq):
        count += 1

# Print the result
print(f"The target sequence appeared {count} times in the FASTA file.")
