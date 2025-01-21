from Bio import SeqIO

# Input FASTA files
file1 = "01_NewReverseBoth_MCF10A.fasta"
file2 = "01_NewBoth_MCF10A.fasta"
output_file = "01_Combined_MCF10A.fasta"

# Open the output file in write mode
with open(output_file, "w") as output_handle:
    # Parse and write the sequences from the first file
    for record in SeqIO.parse(file1, "fasta"):
        SeqIO.write(record, output_handle, "fasta")

    # Parse and write the sequences from the second file
    for record in SeqIO.parse(file2, "fasta"):
        SeqIO.write(record, output_handle, "fasta")

print(f"Combined sequences have been saved to {output_file}")