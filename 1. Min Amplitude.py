"""Question 1:
Given an Array A, find the minimum amplitude you can get after changing up to 3 elements. Amplitude is the range of
the array (basically difference between largest and smallest element).

Example 1:

Input: [-1, 3, -1, 8, 5 4]
Output: 2
Explanation: we can change -1, -1, 8 to 3, 4 or 5

Example 2:

Input: [10, 10, 3, 4, 10]
Output: 0
Explanation: change 3 and 4 to 10"""


def minAmp(arr):

    if len(arr)<=4:
        return 0
    arr.sort()
    #minAmp=max(arr)-min(arr)

    #option1 remove 3 element on the left
    option1Amp=max(arr[3:])-min(arr[3:])

    # option2 remove 3 element on the right
    option2Amp = max(arr[:-3])- min(arr[:-3])

    #option3: remove 2 Left, 1 right
    option3Amp = max(arr[2:-1]) - min(arr[2:-1])

    # option3: remove 1 Left, 2 right
    option4Amp = max(arr[1:-2]) - min(arr[1:-2])
    minAmp=min(option1Amp,option2Amp,option3Amp,option4Amp)

    return minAmp



assert (2 == minAmp([-1, 3, -1, 8, 5, 4]))
assert (0 == minAmp([10, 10, 3, 4, 10]))
