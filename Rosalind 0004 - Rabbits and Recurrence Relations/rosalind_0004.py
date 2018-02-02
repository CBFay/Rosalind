# http://rosalind.info/problems/fib/
# Calculate n'th values in recurrence sequences
# Created 2.1.2018 by CB Fay

N = int(input("n: "))
K = int(input("k: "))

def rabbits(n, k):
    a = 0
    b = 1
    for i in range(n):
        a, b = b, b + (a * k)
    return a

print(rabbits(N, K))
