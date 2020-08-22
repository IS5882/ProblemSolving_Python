A=["Shogun", "Tapioca Express", "Burger King", "KFC"]
D=["KFC", "Shogun", "Burger King"]
#A=["Shogun","Tapioca Express","Burger King","KFC"]
#D=["KFC","Burger King","Tapioca Express","Shogun"]
#A=["Shogun","Tapioca Express","Burger King","KFC"]
#D=["KNN","KFC","Burger King","Tapioca Express","Shogun"]

dlen=len(D)
alen=len(A)
indexSum=0
num={}
sameS=""
sameScore=0

if (sorted(A)== sorted(D)):
    print(A)

else:
    for i in range(alen):

       for j in range(dlen):
          #print(D[j])
          if A[i] == D[j]:
           #print(A[i])
           indexSum=i+j
           if(indexSum in num):
               print(" same score")
               sameScore=indexSum
               sameS=sameS+" "+(A[i])
           else:
               num[indexSum]=(A[i])

    for n in num:
        if n != None and n<sameScore:
        #if n != None:

          print(num[n])
          print(n)
          break
        elif sameScore>= n:
            print(sameS)
            break
        break
    print(sameScore)

"""
leetcode

    def findRestaurant(self, list1, list2):
        if (sorted(list1)== sorted(list2)):
         return(list1)
        dlen=len(list2)
        alen=len(list1)
        indexSum=0
        num={}
        for i in range(alen):
         for j in range(dlen):
           if list1[i] == list2[j]:
             indexSum=i+j
             num[indexSum]=(list1[i])

        for n in num:
           if n != None:
            return([num[n]])
"""