#!/usr/local/bin/python3

inputfile = open('rosalind_gc.txt', 'r')

fasta_data = inputfile.read().strip()

# Parse the FASTA data into a dict
dna_strings = {}

currentKey = ""
for line in fasta_data.split("\n"):
	if (line[0] == ">"):
		currentKey = line
		dna_strings[currentKey] = ""
	else:
		dna_strings[currentKey] += line

gc_occurrences = {}
gc_counter = 0
for key in dna_strings:
	for letter in dna_strings[key]:
		if letter == "G" or letter == "C":
			gc_counter += 1
	gc_ratio = gc_counter / len(dna_strings[key]) * 100
	gc_occurrences[key] = round( gc_ratio , 7 )
	gc_counter = 0


max_string = max(gc_occurrences, key=gc_occurrences.get )
max_string_clean = max_string.replace(">", "")
print(max_string_clean)
print(gc_occurrences[max_string])
