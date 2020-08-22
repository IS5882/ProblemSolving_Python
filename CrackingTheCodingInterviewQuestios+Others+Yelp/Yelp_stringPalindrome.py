strs="tocacot"
mid=int(len(strs)/2)


if(len(strs)==1):
    print("its 1 letter %s" %strs)
print(strs[:mid])
print(reversed(strs[-mid:]))

if(strs[0:mid] != ("".join(reversed(strs[-mid:])))):
         print("not palindrome")
else:
    print("palidrome")
