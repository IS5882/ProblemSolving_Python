"""https://leetcode.com/discuss/interview-question/922076/Google-or-Phone-(London)-or-Maximize-sum-with-multiplier-array
You are given one more array of size K. This array is called a multiplier array. First element will get
multiplied with the first number chosen. Your task is to maximise the sum of the numbers. In short :

A : [2,13,7,15]
B : [2,3]

You can choose :
1- 2 * 2 + 13 * 3 or
2- 2 * 2+ 15 * 3 or
3- 15 * 2 + 2 * 3 or
4- 15 * 2 + 7 * 3

Another example :
A: [-2,8,1,15,-6]
B: [3,2,5]

1: -2 * 3 + 8 * 2 + 1 * 5 or
2: -2 * 3 + -6 * 2 + 15 *5
[...]

(In short you've to choose from Left or Right on the array A the amount of number of elements for B.length which multiplied for elements in A will maximize the sum )

Array A has no constraint (It could filled also with negative numbers)
"""

import collections
def maximizeSum(A,B):
    maxSum=float('-inf')
    q=collections.deque()
    q.append((0,len(A)-1,0,0)) #A start, A end, B start, Val
    while q:
        idxA,endA,idxB,val=q.popleft()
        #print('idxA',idxA,'endA',endA,'idxB',idxB,'val',val)
        if idxB==len(B):
            maxSum=max(maxSum,val)

        else:
            q.append((idxA+1,endA,idxB+1,val+(A[idxA]*B[idxB])))
            q.append((idxA,endA-1,idxB+1,val+(A[endA]*B[idxB])))
    return maxSum

A=[2,13,7,15]
B=[2,3]
print('maxSum',maximizeSum(A,B))


A=[0,-1,1,-1]
B=[2,3]
print('maxSum',maximizeSum(A,B))


A=[-1,-2,-1,-1]
B=[2,3]
print('maxSum',maximizeSum(A,B))




