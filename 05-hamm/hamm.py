#!/usr/local/bin/python3

inputfile = open('rosalind_hamm.txt', 'r')

dna_data = inputfile.read().strip().split("\n")

if len(dna_data[0]) != len(dna_data[1]):
	print("ERROR - The two dna inputs have different length")
	exit(1)

hamming_dist = 0
counter = 0
for base in dna_data[0]:
	if base != dna_data[1][counter]:
		hamming_dist += 1
	counter += 1

print(hamming_dist)
