# http://rosalind.info/problems/hamm/
# Determine the hamming distance between two strings
# Created 2.1.2018 by CB Fay

with open("rosalind_hamm.txt") as file:
    a, b = file.read().splitlines()
    print(len([i for i in range(len(a)) if a[i] != b[i]]))
