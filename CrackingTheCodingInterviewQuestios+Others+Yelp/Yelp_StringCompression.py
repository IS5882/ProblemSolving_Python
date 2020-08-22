s=("aabbbccccaffcccccccc")

j=0
a=""
length=len(s)
i=0
while i in range(length):
    count=1
    a=a+s[i]
    while (j<(len(s)-1) and s[i] in s[j+1]):
        count=count+1
        j=j+1
    else:
        a = a + ('%s' % count)
        j=j+1
        i=i+count
    print(j)




print(s)
print(a)


