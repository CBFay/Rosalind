# http://rosalind.info/problems/iprb/
# Created 2.5.2018 by CB Fay

with open('rosalind_iprb.txt') as file:
    K, M, N = [int(n) for n in file.read().split(' ')]
    # K: Number of homozygous dominants
    # M: Number of heterozygous
    # N: Number of homozygous recessives

def main():
    print(dominant_phenotype(K, M, N))

def dominant_phenotype(k, m, n):
    total = k + m + n
    
    """The probabilities of getting a specific pairing
    AND that pairing producing a dominant phenotype."""
    pair_probability = {
    'kk' : k/total * (k-1)/(total-1) * 1.0,
    'mm' : m/total * (m-1)/(total-1) * .75,
    'nn' : n/total * (n-1)/(total-1) * 0.0,
        
    'km' : k/total * m/(total-1) * 1.0,
    'mk' : m/total * k/(total-1) * 1.0,
        
    'kn' : k/total * n/(total-1) * 1.0,
    'nk' : n/total * k/(total-1) * 1.0,
        
    'mn' : m/total * n/(total-1) * .50,
    'nm' : n/total * m/(total-1) * .50
    }
    
    """OR"""
    dom_presence = sum(pair_probability.values())
    return round(dom_presence, 5)
    
if __name__ == '__main__':
    main()
    
