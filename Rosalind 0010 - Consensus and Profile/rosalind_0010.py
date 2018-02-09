# http://rosalind.info/problems/cons/
# Find a likely common ancestor
# Created 2.8.2018 by CB Fay

# Format input
with open('rosalind_cons2.txt') as file:
    dna = []
    labels = []
    
    for line in file.read().splitlines():
        if line[0] == '>':
            labels.append(line)
            dna.append('')
        else:
            dna[-1] += line

# Populate a profile matrix
size = len(dna[0]) # helper variable
profile = dict(zip((b for b in 'ACGT'), ([0] * size for i in range(4))))
for sample in dna:
    for i in range(size):
        profile[sample[i]][i] += 1
    
# Build a concensus list
consensus = "".join([max(profile, key=(lambda k: profile[k][i])) \
             for i in range(size)])
    
# Format output
print(consensus)
for base in profile:
    print(base + ':', " ".join(str(n) for n in profile[base]))
