#!/usr/local/bin/python3

inputfile = open('rosalind_dna.txt', 'r')

dna_data = inputfile.read()
dna_data = dna_data.replace("\n", "")
print(dna_data)

letters = {"A": 0, "T":0, "C": 0, "G": 0}

for l in dna_data:
	letters[l] += 1

print(f"{letters['A']} {letters['C']} {letters['G']} {letters['T']}")
