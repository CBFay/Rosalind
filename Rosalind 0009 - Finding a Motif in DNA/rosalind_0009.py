# http://rosalind.info/problems/subs/ 
# Return indices of a substring within a string
# Created 2.7.2018 by CB Fay

def main():
    with open('rosalind_subs.txt') as file:
        S, T = file.read().splitlines()
        print(substring_search(S, T))
        
def substring_search(s, t):
    return " ".join([str(i+1) for i in range(len(s)) if s[i:i+len(t)] == t])

if __name__ == '__main__':
    main()
