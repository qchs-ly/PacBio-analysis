from Bio import SeqIO

# Path to your FASTA file
fasta_file = "05_MCF7_AA.fasta"

# Define valid amino acid characters
valid_amino_acids = set("ARNDCEQGHILKMFPSTWYV")

try:
    # Try parsing the FASTA file
    for record in SeqIO.parse(fasta_file, "fasta"):
        # Check if the sequence contains invalid characters
        invalid_chars = set(str(record.seq).upper()) - valid_amino_acids
        if invalid_chars:
            print(f"Invalid characters {invalid_chars} found in sequence {record.id}")
    print("FASTA file is properly formatted.")
except Exception as e:
    print(f"Error parsing FASTA file: {e}")

