#!/usr/local/bin/python3

inputfile = open('rosalind_revc.txt', 'r')

dna_data = inputfile.read()
dna_data = dna_data.replace("\n", "")

dna_complement = ""
complement_table = {
	"A": "T",
	"T": "A",
	"C": "G",
	"G": "C"
}

for base in dna_data:
	dna_complement += complement_table[base]

reversed_compl =''.join(reversed(dna_complement))
print(reversed_compl)
