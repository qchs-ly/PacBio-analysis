from Bio import SeqIO

# Define the possible barcodes for MCF-7 and MCF10A
mcf7_barcodes = ["ACACCCGGAATAAATCGCAGG", "GGACGCTAAATAAGGCCCACA", "TGTGGGCCTTATTTAGCGTCC", "CCTGCGATTTATTCCGGGTGT"]
mcf10a_barcodes = ["CATCCCGGAATAAATCGCAGG", "GGACGCTAAATAAGGCCCTAC", "GTAGGGCCTTATTTAGCGTCC", "CCTGCGATTTATTCCGGGATG"]

# Input FASTA file
input_fasta = "01_Combined.fasta"

# Output FASTA files for MCF-7 and MCF10A
output_mcf7 = "01_MCF7_sequences.fasta"
output_mcf10a = "01_MCF10A_sequences.fasta"

# Open output files
with open(output_mcf7, "w") as mcf7_out, open(output_mcf10a, "w") as mcf10a_out:
    # Parse the input FASTA file
    for record in SeqIO.parse(input_fasta, "fasta"):
        sequence = str(record.seq)
        # Check if the sequence contains any of the MCF-7 barcodes
        if any(barcode in sequence for barcode in mcf7_barcodes):
            SeqIO.write(record, mcf7_out, "fasta")
        # Check if the sequence contains any of the MCF10A barcodes
        elif any(barcode in sequence for barcode in mcf10a_barcodes):
            SeqIO.write(record, mcf10a_out, "fasta")