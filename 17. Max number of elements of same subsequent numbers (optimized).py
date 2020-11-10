

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
    myC = collections.Counter()
    maxf = p1 = p2 = 0

    while p2 < len(nums):
        myC[nums[p2]] += 1
        maxf = max(maxf, myC[nums[p2]])

        if p2 - p1 + 1 > maxf + 3:
            myC[nums[p1]] -= 1
            p1 += 1
        p2 += 1
    return len(nums) - p1

A=[[3,1,3,2,5,3],[3,1,3,2,5,1,9,7],[0,0,1,1,1,0],[2,1,2,2,3],[1,1,2,2,2,2,2,3,5] ]


for nums in A:
    print('nums is',nums,'max sub is',maxSub(nums))
