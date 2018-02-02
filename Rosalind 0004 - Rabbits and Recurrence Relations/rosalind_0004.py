# http://rosalind.info/problems/fib/
# Calculate n'th values in recurrence sequences
# Created 2.2.2018 by CB Fay

file = open("rosalind_fib.txt")
text = file.read().split(" ")
file.close()

N = int(text[0])
K = int(text[1])

def population(n, k):
    m = 0 # mating
    p = 1 # pairs
    for i in range(n):
        m, p = p, p+(m*k)
    return m

print(population(N, K))
