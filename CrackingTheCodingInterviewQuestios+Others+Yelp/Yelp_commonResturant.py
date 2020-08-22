A=["Shogun", "Tapioca Express", "Burger King kooo", "KFC"]
D=["KFC", "Shogun", "Burger King"]

for i in A:
    for j in D:
        if (i == j):
            print(i)



x=set(A)
print(set(A).intersection(D))
print(set(A).union(D))