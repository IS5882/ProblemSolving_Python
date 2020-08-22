S="a1b2C"
"""
a=s+' '+s.swapcase()
print(s.capitalize())
print(a)

b=s

for i in s:
    b=b+''+i.swapcase()

print (b)

x = (s + ' ' + s.swapcase() + ' ' + s.upper() + ' ' + s.lower())
print(x)
"""
res=[""]

for s in S:
            if s.isalpha():
                res = [word + j for word in res for j in [s.lower(), s.upper()]]
            else:
                res = [word + s for word in res]

print(res)
"""
x=S
l=len(S)
for s in S:
    if s.isalpha():
        x=[x +' '+ for word in res for j]
"""