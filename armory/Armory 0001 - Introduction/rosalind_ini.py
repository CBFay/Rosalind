# http://rosalind.info/problems/ini/
# Introduction to BioPython
# Created 2.12.2018 by CB Fay

from Bio.Seq import Seq

def main():
    seq = read('rosalind_ini.txt')
    base_frequency(seq)

def read(filename):
    with open(filename) as file:
        return file.read()

def base_frequency(sequence):
    s = Seq(sequence)
    print(s.count('A'), s.count('C'), s.count('G'), s.count('T'))
        
if __name__ == '__main__':
    main()