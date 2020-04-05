#!/usr/local/bin/python3

inputfile = open('rosalind_prtm.txt', 'r')

aa_data = inputfile.read().strip()

# store the weight of water
h2o_weight = 18.01056

# parse the amino acid weight values and store them into a dictionary
monoisotropic_mass_table = """
A   71.03711
C   103.00919
D   115.02694
E   129.04259
F   147.06841
G   57.02146
H   137.05891
I   113.08406
K   128.09496
L   113.08406
M   131.04049
N   114.04293
P   97.05276
Q   128.05858
R   156.10111
S   87.03203
T   101.04768
V   99.06841
W   186.07931
Y   163.06333
"""

monoisotropic_mass_arr = monoisotropic_mass_table.strip().replace("   ", " ").split("\n")
monoisotropic_mass_dict = {}

for massdata in monoisotropic_mass_arr:
    split_data = massdata.split(" ")
    monoisotropic_mass_dict[split_data[0]] = split_data[1]

# calculate the protein mass of the aa string given
protein_mass = 0
for aa in aa_data:
    protein_mass += float(monoisotropic_mass_dict[aa])

protein_mass = round(protein_mass, 3)

# print the result
print(protein_mass)
