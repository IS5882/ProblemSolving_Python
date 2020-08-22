#strs=["ABCD", "ABCE", "ACF","AB"]
strs=["mqwasfsafsafe","mqwaasfsafsaf","mqwasfsafsaf","mqwhyyyyassfsf"]

p=strs[0]
mins=min((strs))
print(mins)

maxs=max((strs))
print(maxs)
pre=""
#now I can only work with min and max then my idea is strip from max
if not strs:
    print ("no string")
for i in range(min(len(mins),len(maxs))):
    #print(i)
    if(mins[i]==maxs[i]):
        pre=pre+mins[i]
        print(mins[i])
    else:
        break #if an in seq element is not common no need to continue with for loop


print(pre)
"""print(sorted(strs))
print(p[-1])
print("-----")
j=len(p) #=4
print(j)
for i in strs[1:]:
    print(i)
    while(j>1 and j<=len(i)):
     if (p[-1] != i[j-1]):
        p=p[:-1]
        print(p)
     elif (p == i[0:j-1]):
       j=j+1
       break
     j=j-1
    break



print(p)"""


"""
for i in strs:
    #print(i)
    #for j in i:
    #    print (j)
    j=0
    p.append(i[0])
    while j<len(i)-1:
        if p == i[j+1]:
           p.append(i)
        j=j+1
print(p)

 #the LCP is "A"

"""

