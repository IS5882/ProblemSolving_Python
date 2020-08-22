from collections import defaultdict
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
dict=defaultdict(list)


print(strs)
print(len(strs))


#put in dict key=sorted word, value =  words with same angrams,

for i in range(len(strs)):
    j=i+1
    print(i)
     #a[i]=strs[i]
    a = ''.join(sorted(strs[i]))
    if (a not in dict.keys()):
     dict[a].append(strs[i])
     while j < (len(strs)):
        #print(strs[i])
        #print(strs[j])
        #print("----")
        if(sorted(strs[i])==sorted(strs[j])):
         print("ANAGRAMMMM")
         dict[a].append(strs[j])
            #a[i]=a[i]+","+strs[j]
        j=j+1


print (dict.values())
"""
for i in range(len(strs)):
    #print (i)

    while j< (len(strs)-1):
       if (sorted(strs[i]) == sorted(strs[j])):
           a[i]=a[i]+(', ')+(strs[j])
       j=j+1

for i in range(len(strs)):
    if(strs[i] not in a):
     j=i+1
     a[i]=strs[i]
     while j < len(strs):
        print(strs[i])
        print(strs[j])
        print("----")
        if(sorted(strs[i])==sorted(strs[j])):
            print("ANAGRAMMMM")
            a[i]=a[i]+","+strs[j]
        j=j+1

print (a)
"""