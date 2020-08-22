#Reduce a 2D array where you need to sum the same elements and return them sorted by amount  
from collections import defaultdict
import itertools

T = [[12, 5, 2], [15, 6, 10], [10, 2, 5]]
a = dict()
for i in range(len(T)):
    for j in range(len(T[i])):
        if T[i][j] in a:
            a[T[i][j]] += 1
        else:
            a[T[i][j]] = 1
#
b = list(a.items())
# sort by
b.sort(key=lambda e: e[1], reverse=True)
print(b)

c = []
for x in b:
    c.append(x[0] * x[1])
print("OUTPUTTTT")
print(c);

#------Remove duplicate chars from list K-------

k = [[1, 2], [4], [5, 6, 2], [1, 2], [3], [4]]
k.sort()
list(k for k,_ in itertools.groupby(k))
print(k)
print(list(k for k,_ in itertools.groupby(k)))
#------Remove duplicate chars from string-------
foo = "SSYYNNOOPPSSIISS"
print(''.join(ch for ch, _ in itertools.groupby(foo)))
#------Remove duplicate words from string-------

string1 = "calvin klein design dress calvin klein"
words = string1.split()
print (" ".join(sorted(set(words), key=words.index)))
"""
i=0
j=0
a=[0]*9
a[0] = T[0][1]

for i in range(len(T)):
    print(T[i])
    for j in range(len(T[i])):
        print(T[i][j])
        if T[i][j] in a:
            a[T[i][j]]=T[i][j]
        print(a)

print("output")
print(a)
"""