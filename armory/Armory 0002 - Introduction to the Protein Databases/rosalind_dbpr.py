# http://rosalind.info/problems/dbpr/
# Determine biological processes associated with a Protein
# Created 2.9.2018 by CB Fay

from Bio import ExPASy
from Bio import SwissProt

proteins = 'L7QHU5'

handle = ExPASy.get_sprot_raw(proteins)
record = SwissProt.read(handle)

cr = record.cross_references
processes = [ref[2][2:] for ref in cr if ref[0] == 'GO' and ref[2][0] == 'P']

for pr in processes:
    print(pr)

    

