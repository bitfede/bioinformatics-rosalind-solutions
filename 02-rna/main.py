#!/usr/local/bin/python3

inputfile = open('rosalind_rna.txt', 'r')

rna_data = inputfile.read()
rna_data = dna_data.replace("\n", "")
print(rna_data)

