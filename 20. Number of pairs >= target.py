"""https://leetcode.com/discuss/interview-question/915403/Google-or-Onsite-or-Number-of-Pairs-Sum-Greater-or-Equal-Target
Given a sorted list of numbers and a target Z, return the number of pairs according to following definition: (X,Y) where X+Y >= Z

Example 1:

Input: arr = [1, 3, 7, 9, 10, 11], Z = 7
Output: 14 """

def numberOfPairs(nums,target):
    p1=0
    p2=len(nums)-1
    pairs=0
    while p1<p2:
        if nums[p2]+nums[p1]>=target:
            pairs+=p2-p1
            p2-=1
        else:
            p1+=1
    return pairs


print('no of pairs',numberOfPairs([1, 3, 7, 9, 10, 11],7)) #14
print('no of pairs',numberOfPairs([1, 11],7)) #1
print('no of pairs',numberOfPairs([0,1],7)) #0
print('no of pairs',numberOfPairs([0,1,2,2],2)) #5


