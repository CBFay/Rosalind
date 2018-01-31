# Created 1.31.2018 by CB Fay

with open('rosalind_dna.txt') as file:
    s = file.read()
    print(s.count('A'), s.count('C'), s.count('G'), s.count('T'))
