S= "hello how are you"
"""print (S)

l=len(S) #num of chars

print (l)
X=S.split(' ') #split by white spaces
print (X)

A=["" for x in range(len(X))]
print(len(X))
i=len(X)
j=0
for v in X:
    A[j] = X[i-1]
    i=i-1
    j=j+1

print(A)
#=======
"""
#print (S)
A=S.split()
#X=[]
A.reverse()
print (' '.join(A))

"""lindt Code
 def reverseWords(self, s):
     words = s.split()
     words.reverse()
     return ' '.join(words)
     """