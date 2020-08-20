def largest_subarray(a, k):

    maxStart=float('-inf')

    p1=0
    p2=k-1 #3

    while p2<len(a):

        if a[p1]>maxStart: #1>-inf
            maxStart=a[p1]
            startIdx=p1
            endIdx=p2

        p1+=1
        p2+=1

    return a[startIdx:endIdx+1]


assert (largest_subarray([1,4,3,2,5],4)==[4,3,2,5])
assert (largest_subarray([1,4,3,2,5],3)==[4,3,2])
assert (largest_subarray([10,1,4,3,2,5],2)==[10,1])