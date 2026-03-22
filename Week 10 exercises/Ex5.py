codon_table = {
    "ATG": "Methionine",
    "GCG": "Alanine",
    "TCC": "Serine",
    "TAT": "Tyrosine",
    "CGT": "Arginine"
}
dna_sequence = "ATGCGTTATGCG"
splitted_list = []
result = []
for i in range(0,len(dna_sequence),3):
    splitted_list.append(dna_sequence[i:i+3])
for i in range(len(splitted_list)):
    for codon , amino_acid in codon_table.items():
        if splitted_list[i] == codon:
            result.append(amino_acid)
print("-".join(result))