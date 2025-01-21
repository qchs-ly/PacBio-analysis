from Bio import SeqIO
from Bio.Seq import Seq

# Input and output FASTA file paths
input_fasta = "NewReverseBoth.fasta"
output_fasta = "NewReverseBothReverse.fasta"

# Open output FASTA file for writing
with open(output_fasta, "w") as output_handle:
    # Parse the input FASTA file
    for record in SeqIO.parse(input_fasta, "fasta"):
        # Get the reverse complement of the sequence
        record.seq = record.seq.reverse_complement()
        # Write the reverse complement sequence to the output file
        SeqIO.write(record, output_handle, "fasta")

print(f"Reverse complement sequences have been saved to {output_fasta}")