"""https://leetcode.com/discuss/interview-question/917409/Google-or-Phone-or-Longest-Subarray-Sum-at-Most-K
int[] arr = {1, 2, 1, 0, 1, -8, -9, 0};
int k = 4;
Output is 8
find the longest subarray whose sum is less or equal to K


int arr[] = {1, 2, 1, 0, 1, 1, 0};
int k = 4;
output is 5



, O(n) time and O(n) space. Please let me know if it is wrong

Keep track of negative cummalative sum from the right end, ie, if cummulative sum becomes positive we reset it to 0

Then use a sliding window to move from left to right:

if sum(window)+neg_cumm_sum[j] <=k, we increment size of window to right
else we shrink it from left
Dry run would look like below

Credits to abinpaul1

"""
import itertools
from  collections import deque
def maxSubarrayLength(nums,k): #{1, 2, 1, 0, 1, 1, 0}
    neg_sum = [0] * len(nums)
    cumm_sum = 0
    for ind, num in enumerate(nums[::-1]):
        neg_sum[ind] = cumm_sum
        cumm_sum += num
        if cumm_sum > 0:
            cumm_sum = 0
        #print('neg_sum now',neg_sum)
    neg_sum = neg_sum[::-1]
    print('neg sum',neg_sum)
    i, j = 0, 0
    N = len(nums)
    max_len = 0
    cumm_sum = 0
    while j < N:
        cumm_sum += nums[j]
        if cumm_sum + neg_sum[j] <= k:
            max_len = max(max_len, j - i + 1)
            j += 1
        else:
            if i != j:
                while cumm_sum + neg_sum[j] > k and i < j:
                    cumm_sum -= nums[i]
                    i += 1
                ## Remove nums[j] from cumm_sum, because we will process it again in loop
                cumm_sum -= nums[j]
            else:
                cumm_sum = 0
                i += 1
                j += 1
    return max_len


print(maxSubarrayLength([1, -2, 1, 20, 1, -8, -9, 0],3)) #should output 7

#print(maxSubarrayLength([1, 2, 1, 0, 1, -8, -9, 0],4)) #should output 8
#print(maxSubarrayLength([1, 2, 1, 0, 1, 1, 0],4)) #should output 5
#print(maxSubarrayLength([1, -2],3)) #should output 2
#print(maxSubarrayLength([1, -2],-5)) #should output 0
print(maxSubarrayLength([9,1, 1,-2,8],5)) #should output 3




"""maxd = deque()
    mind = deque()
    i = 0
    res = 0
    for j, a in enumerate(nums):
        # print('a',a,'i',i)
        while maxd and a > maxd[-1]: maxd.pop()
        while mind and a < mind[-1]: mind.pop()
        maxd.append(a)
        mind.append(a)
        print(' maxd', maxd)
        print(' mind', mind)
        print('maxd[0] + mind[0]',maxd[0] + mind[0])
        diff=maxd[0] - mind[0]
        if diff<=k:
            res = max(res, j - i + 1)

        else:
            print('yes will pop',maxd[0], mind[0])
            if maxd[0] == nums[i]: maxd.popleft()
            if mind[0] == nums[i]: mind.popleft()
            i += 1
            print('updated maxd',maxd)
            print('updated mind',mind)
    return res"""