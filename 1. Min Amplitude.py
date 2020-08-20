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
"""
    currMaxAmp=abs(max(arr)-min(arr)) #8--1=9
    arr.sort() #[-1 -1 3 4 5 8]
    count=0
    #index=[]
    idx=0
    #for idx,num in enumerate(arr):
    #for idx in range(len(arr)):
    while idx<len(arr):
        print('idx is',idx)
        if abs(max(arr)-min(arr))>=currMaxAmp:
            print('yes',currMaxAmp)
            #either change the min or max, test the removal of both and decide
            count+=1
            option1=min(arr[idx+1:]) #option1:change the min element
            print('option1 so the new min is',option1)
            option2=max(arr[:len(arr)-1]) #option2: change the max elment
            print('option2 so the new max is', option2)
            print('new amp with option1 ',abs(max(arr)-option1))
            print('new amp with option2 ', abs(min(arr)-option2))
            if abs(max(arr)-option1) <= abs(min(arr)-option2): # We want to remove the one that will result in the highest ampthen change option1
                print('will go with option1 ')
                arr=arr[:idx]+arr[idx+1:] #changing asif removing the element

            else:
                print('will go with option2 ')
                arr=arr[:len(arr)-1]
            print('arr now is',arr)
            currMaxAmp = abs(max(arr) - min(arr))
            print('new currMaxAmp',currMaxAmp)

        else:
            idx+=1

        if count==3:
            newAmp=max(arr)-min(arr)
            print('newAmp',newAmp)
            return max(arr)-min(arr)
"""
"""    for idx,num in enumerate(arr):

        if max(arr)-num>=currMaxAmp:
            index.append(idx) #[0,1,
            currMaxAmp=max(arr)-min(arr[idx:]) #
            count+=1
        if count==3:
            break"""



