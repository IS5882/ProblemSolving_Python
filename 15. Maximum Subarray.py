""" so the new subarray -> the largest as possible

Has K element
# of elements >K == #of elements <K, if num=K we can leave it in the subarray

[5,7,5,4,5,8,2] --> K=5 --> ans=7 already satisfying the result

[5,9,7,8,2,4] ---> K=5 --> [5,7,8,2,4] = 5

[5,7,2,8,7,4,5,9] --> K=5 --> [5,7,2,4,5,9] =6

Convert the array element like -->greater than K with 1 ,smaller than K with -1,equal to K with 0
Eg - [5,9,7,8,2,4]--- >[0,1,1,1,-1,-1] It will be easy for checking out the numbers
Now we have to find min subarray length with sum equal to cumulative sum of new array
[0,1,1,1,-1,-1] sum is 1--> so this will be the deleted subarray

min subarray length equal to cumulative sum is 1 (Because we have maximize the length of array after deletion )
Answer will be arr.size()-min_sub_length
output: 5
Complexity :O(n) Time and Space
Hope it's help
"""
import collections
def maxSubarray(nums,K):

    for i in range(len(nums)):
        if nums[i]>K:
            nums[i]=1
        elif nums[i]<K:
            nums[i]=-1
        else:
            nums[i]=0


    # dictionary mydict implemented
    mydict = {}

    # Initialize sum and maxLen with 0
    total = 0
    findSum = sum(nums)
    minDeletion = float('inf')
    if findSum==0:
        return len(nums)
    print('nums',nums)
    print('FindSum',findSum)
    # traverse the given array
    for i in range(len(nums)):

            # accumulate the sum
            total += nums[i]
            print('i is=',i,'total is',total)
            # when subArray starts from index '0'
            if (total == findSum):
                #minDeletion=min(len(nums)-i,minDeletion)
                print('Sum is found between 0 and ',i)
                minDeletion = min(i+1, minDeletion)
                #print('minDeletion is now is',minDeletion)
            # check if 'sum-k' is present in
            # mydict or not
            if (total - findSum) in mydict:
                minDeletion = min(minDeletion, i - mydict[total - findSum])

                # if sum is not present in dictionary
            # push it in the dictionary with its index
            #if total not in mydict:
            mydict[total] = i
            print('minDeletion is now is', minDeletion)
            print('dict is',mydict)
    answer = len(nums) - minDeletion

    print(minDeletion)
    return answer

assert (maxSubarray([5,7,5,4,5,8,2],5)==7)
assert (maxSubarray([5,9,7,8,2,4],5)==5)
assert (maxSubarray([5, 7, 2, 8, 7, 4, 5, 9], 5) == 6)

"""
    p1=0
    p2=0
    total=0
    findSum=sum(nums)
    minDeletion=float('inf')
    print('nums',nums)
    print('FindSum',findSum)

    while p2<len(nums) and p1<len(nums):
        total=total+nums[p2]
        print('total =',total)

        if total<findSum:
            p2+=1
        else:
            minDeletion=min(minDeletion,p2-p1+1)
            print('minDel',minDeletion)
            total=total-nums[p2]-nums[p1]
            p1+=1
    """

