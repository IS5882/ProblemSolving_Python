"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: interval list.
    @return: A new interval list.
    """


    def merge(self, intervals):
        intervals.sort(key=lambda x: x.start)

        merged = []
        for interval in intervals:
            # if the list of merged intervals is empty or if the current
            # interval does not overlap with the previous, simply append it.
            if not merged or merged[-1].end < interval.start:
                merged.append(interval)
            else:
            # otherwise, there is overlap, so we merge the current and previous
            # intervals.
                merged[-1].end = max(merged[-1].end, interval.end)

        return merged
"""
    
#A=[(1, 3), (2, 6), (8, 10), (15, 18), (9,11)]
A=[(1,5),(1,3),(3,5),(6,7),(8,10),(12,16),(4,9)]
print("unsorted")
print(A)
 
print (A)
print (A[0]) #to get both elements: the whole interval
print (A[0][0]) #to get 1st element

print(len(A))
#for i in A:
    # print (i)    #to get both elements: the whole interval
    #print (i[0]) #to get 1st element
    #print(i[1])  #to get 2nd element
    #j=i+1;
  #  while (i[1]) > i:
   #     print ("2nd el. is bigger than 1st el of next interval ")
X=[]
j=1
#X.append([1,8])
#X.append([1,8])

for i in A:
  for j in range(len(A)-1):
      y=j+1
      if i[1] > A[j+1][0]:
          print ("START should merge interval")
          print(y)
          print(i[1])
          print (A[y][0])
          print ("END")
          y=y+1
          #X[y]=[(i[0],A[j][1])]
          X.append([i[0], A[j+1][1]])

print(X)



A.sort()
print("sorted")
print(A)
j=1

merged = []
for interval in A:
            # if the list of merged intervals is empty or if the current
            # interval does not overlap with the previous, simply append it.

    #if not merged:
     #    merged.append(interval)
    if  (interval[1] > A[j][0]):
        merged.append([interval[0],A[j][1]])
    if(j>1):
     if (interval[0] not in merged[0]) or ((interval[0] < A[j][0]) and (interval[1] < A[j][1])):
        merged.append([interval[0],interval[1]])
    #else:
     # otherwise, there is overlap, so we merge the current and previous
     # intervals.
         #merged[-1].end = max(merged[-1].end, interval.end)
    if j < (len(A)-1):
     j=j+1

print(merged)
"""