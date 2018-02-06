# Translate RNA string into the Protein string it will produce
# Created 2.6.2018 by CB Fay

import json

# Load Codon -> Protein dictionary from json
with open('rna_codon_table.json') as table:
    RNA_CODON_TABLE = json.load(table)

# Open RNA string
with open('rosalind_prot.txt') as dataset:
    RNA = dataset.read().strip()
    
# Return the protein string encoded by rna
def translate(rna, table):
    codons = list(rna[i:i+3] for i in range(0, len(rna), 3))
    return "".join(table[c] for c in codons)[:-1] 

def main():
    print(translate(RNA, RNA_CODON_TABLE))

if __name__ == '__main__':
    main()
