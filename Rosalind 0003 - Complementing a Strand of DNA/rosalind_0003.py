# http://rosalind.info/problems/revc/
# Print the reverse compliment of a DNA String
# Created 1.31.2018 by CB Fay

with open('rosalind_revc.txt') as file:
    s = file.read().replace('\n', '')
    pair = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
    print("".join(pair[base] for base in s[::-1]))
