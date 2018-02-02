# http://rosalind.info/problems/gc/
# Find the highest GC-content string from a collection
# Created 2.2.2018 by CB 

def gc_content(s):
    content = s.count("G") + s.count("C")
    ratio = content / len(s) * 100
    return round(ratio, 4)

data = []
with open("rosalind_gc.txt") as file:
    text = file.readlines()

for line in text:
    if line[0] == '>':
        data.append([line[1:].strip(), ""])
    else:
        data[-1][1] += line.strip()

maxi =[None, 0]
for entry in data:
    entry[1] = gc_content(entry[1])
    if entry[1] > maxi[1]:
        maxi = entry
        
print(maxi[0])
print(maxi[1])
