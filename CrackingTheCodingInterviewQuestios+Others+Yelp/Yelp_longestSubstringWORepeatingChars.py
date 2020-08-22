from collections import defaultdict
#s="abcabcbb"
#s="bbbdfsbb"
s="an++--viaj"
n = len(s)
print(n)
if n == 0:
    print("no string")
longest = 1
subs = [s[0]]
for i in range(1, n):
    c = s[i]
    #print(i)
    #print(c)
    while c in subs: #this while empty sub till the repeated char is no  longer in sub
        #print("in while")
        subs = subs[1:]
        #print(subs)
    subs.append(c) #then it put the char
    #print(subs)
    if len(subs) > longest:
        longest = len(subs)
       # print(longest)
print(longest)
print(subs)
"""
injy attempt 2 also didnt pass all
print(len(s))
a=defaultdict(list)
#a=s[2]
print(a)
#a[0] = s[0]+s[1]
print(a)
j=0
for i in range(len(s)):
    if (s[i] not in a[j]):
        a[j].append(s[i])
    else:
        j=j+1
        a[j].append(s[i])
        
print(a)
print(len(a))
print(max(a))
print(min(a))
maxx=len(a[0])
print(maxx)

for y in range(len(a)):
    if(len (a[y]) > maxx):
     maxx=len (a[y])

print(maxx)
        
"""

#a=[a+ s[i] if s[i] not in a]
""" did not pass all cases in lint code
a=""
for i in range(len(s)):
    #print(i)
    if(s[i] not in a):
         a=a+s[i]
    print(len(a))    
    
"""
