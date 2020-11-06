"""you have 3 moves. 1 move: changing a number in the array.
what is the maximum number of the same subsequent numbers.

ex: A = [3,1,3,2,5,3] output : 6 A becomes [3,3,3,3,3,3]
you don't need to use all 3 moves

ex: A = [3,1,3,2,5,1,9,7] output : 5 A becomes [3,3,3,3,3,1,9,7]

ex: A = [0,0,1,1,1,0] it becomes al 1s or 0s by using all 3 move. output is 6

if [2,1,2,2,3] —> with 2 moves only I will get output =5

if [1,1,2,2,2,2,2,3,5] —> with 3 moves I will get 8 (since ill have 8 consecutive 2’s)

[1,2,2,1,2,1,1,3,2,3,2,2]
Constraint: Array size wont exceed 10
"""
import collections
def maxSub(nums):

    print('start of fun',nums)
    def check(firstKey,firstVal):

        start=0
        maxL=0

        while start<=len(nums)-firstVal:
            count=0
            moves=3
            for n in nums:
                if n!=firstKey:
                    if moves==0:
                        break
                    moves-=1
                    count+=1


                else:
                    count+=1
            maxL=max(maxL,count)
            start+=1
        return maxL



    myCount=collections.Counter(nums)
    maxRes=0
    while myCount:
        firstKey=next(iter(myCount))
        firstVal = myCount[firstKey]
        res=check(firstKey,firstVal)

        print('firstKey',firstKey,'res',res)
        maxRes = max(maxRes, res)
        if res>=4 and res>=len(nums)-myCount[firstKey]:
            return maxRes
        else:
            myCount.pop(firstKey)
    if len(nums)>=4:
        return max(maxRes,4)
    else:
        return len(nums)



A=[[3,1,3,2,5,3],[3,1,3,2,5,1,9,7],[0,0,1,1,1,0],[2,1,2,2,3],[1,1,2,2,2,2,2,3,5] ]


for nums in A:
    print('nums is',nums,'max sub is',maxSub(nums))
