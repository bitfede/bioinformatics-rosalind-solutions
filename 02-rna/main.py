#!/usr/local/bin/python3

inputfile = open('rosalind_rna.txt', 'r')

dna_data = inputfile.read()
dna_data = dna_data.replace("\n", "")

transcribed_rna = ""

for base in dna_data:
	if base == "T":
		transcribed_rna += "U"
	else:
		transcribed_rna += base

print(transcribed_rna)
