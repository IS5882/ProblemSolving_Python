numbers=[2, 7, 11, 8, 15]
target=9

"""
for i in numbers: 
 print (i.index)
   # if i + (for i+1 in numbers ) = target
    #print ("found")
    
    
      
"""

lib = {}
print(lib)
for i in range(len(numbers)): #to make i loop on each index not each element
    num = numbers[i]
   # print(i, num)
    if target - num in lib:
        print([lib[target - num], i])
    if num not in lib:
        lib[num] = i



