#Read in N Strings in the format of "Restaraunt_ID Restaraunt_Rating" and print out a sorted list with the highest ratings on top.

RR=input("enter Restaraunt_ID Restaraunt_Rating ")
x=RR.split()
print(RR)
y={}
print(x)
i=0

while i< len(x)-1:
    y[int(x[i])]=int(x[i+1])
    i=i+2


print(y)
print(sorted(y.keys()))

#print sorted based on key rest id --key is rest id since rest wont be repeared
print("----sort Keys ASC----")

for key in sorted(y.keys()):
    print ("%s: %s" % (key, y[key]))
print("----sort values DESC----")
#print sorted based on value what I want
for key, value in sorted(y.items(),key=lambda x: x[1], reverse=True):
    print ("%s: %s" % (key, value))

#for  v in sorted(y.values(),reverse=True):
#    print ("%s: %s" % (y.keys(v), y[v]))

#sorted_d =  sorted(y.items(),key=lambda x:sorted(x), reverse=True)
#print(sorted_d)
