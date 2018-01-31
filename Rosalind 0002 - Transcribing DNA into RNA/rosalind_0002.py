# http://rosalind.info/problems/rna/
# Transcribe DNA into RNA
# Created 1.31.2018 by CB Fay

with open('rosalind_rna.txt') as file:
    t = file.read().replace('T', 'U')
    print(t)
