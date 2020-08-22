L1=[11,53,34]
L2=[21,52,10,11]

L3=set(L1)

print(L1)
print(L2)
print(L3)

L3.update(L2)

print(L3)
print(sorted(L3))
print(sorted(L3, reverse=True))
x=sorted(L3, reverse=True)
print(x)