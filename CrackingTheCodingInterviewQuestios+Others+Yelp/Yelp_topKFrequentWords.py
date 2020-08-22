from collections import defaultdict
words=[
    "yes", "lint", "code",
    "yes", "code", "baby",
    "you", "baby", "chrome",
    "safari", "lint", "code",
    "body", "lint", "code"]

k=3
dict=defaultdict(list)
count=[0]*len(words)

for i in words:
    #print(i)
    for j in range(len(words)):
        if i == words[j]:
            count[j]=count[j]+1
            dict[i]=count[j]
print(count)
print(dict)

for n in range(0,k):
 print(max(dict, key=dict.get))
 dict.pop(max(dict, key=dict.get))

