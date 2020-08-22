o=-8339
if o < 0:
    n=o*-1
nn=str(n)
size=len(nn)
mid=int(len(str(nn))/2)
nd=nn
ni=nn

if(len(nn)==1):
    print("its 1 digit %s" %nn)

      #if we increment
while(ni[0:mid]!=("".join(reversed(ni[-mid:])))):
         ni = int(ni) + 1
         ni = str(ni)
      #if we decrement
while (nd[0:mid] != ("".join(reversed(nd[-mid:])))):
         nd = int(nd) - 1
         nd=  str(nd)
if o < 0:
    print("yes")
    ni=int(ni)*-1
    nd = int(nd)*- 1
if(int(ni)-int(o) < int(o)-int(nd)):
        print(ni)
else:
       print(nd)