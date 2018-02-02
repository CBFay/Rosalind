# http://rosalind.info/problems/fib/
# Calculate n'th values in recurrence sequences
# Created 2.1.2018 by CB Fay

file = open("rosalind_fib.txt").read().split(" ")

N = int(file[0])
K = int(file[1])

def rabbits2(n, k):
    a = 0
    b = 1
    for i in range(n):
        a, b = b, b + (a * k)
    return a

print(rabbits2(N, K))
