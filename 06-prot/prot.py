#!/usr/local/bin/python3

inputfile = open('rosalind_prot.txt', 'r')

dna_data = inputfile.read().strip()

# parse the codon to protein table into a python dictionary
codon_protein_table = """
UUU F,CUU L,AUU I,GUU V
UUC F,CUC L,AUC I,GUC V
UUA L,CUA L,AUA I,GUA V
UUG L,CUG L,AUG M,GUG V
UCU S,CCU P,ACU T,GCU A
UCC S,CCC P,ACC T,GCC A
UCA S,CCA P,ACA T,GCA A
UCG S,CCG P,ACG T,GCG A
UAU Y,CAU H,AAU N,GAU D
UAC Y,CAC H,AAC N,GAC D
UAA Stop,CAA Q,AAA K,GAA E
UAG Stop,CAG Q,AAG K,GAG E
UGU C,CGU R,AGU S,GGU G
UGC C,CGC R,AGC S,GGC G
UGA Stop,CGA R,AGA R,GGA G
UGG W,CGG R,AGG R,GGG G
"""

codon_protein_array = codon_protein_table.strip().replace("\n", ",").split(",")
codon_protein_dict = {}

for x in codon_protein_array:
    codon_prot = x.split(" ")
    codon_protein_dict[codon_prot[0]] = codon_prot[1]

# Check that the RNA string is divisible by 3
if len(dna_data) % 3 != 0:
    exit(1)

# split the dna data into codons and store them into an array
codons_arr = []
counter = 0
while counter < len(dna_data):
    codons_arr.append(dna_data[counter:counter+3])
    counter += 3

# finally convert the codons into an amino acid sequence
protein_sequence = ""
for codon in codons_arr:
    protein = codon_protein_dict[codon]
    if protein != "Stop":
        protein_sequence += codon_protein_dict[codon]

#print the result
print(protein_sequence)






# asd
