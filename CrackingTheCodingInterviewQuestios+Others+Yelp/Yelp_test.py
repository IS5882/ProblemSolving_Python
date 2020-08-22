open_hours=[(8, 14),(18,20)]
j=(10,12)
noOH=[0]*len(open_hours)
#print(noOH)
c=0
d=[]

for i in open_hours:
     print(i)
     noOH[c]=i[1]-i[0]
     c=c+1


print("noOH")
print(noOH)
QueryTime=j[1]-j[0]
print(sum(noOH))
ratio=QueryTime/(sum(noOH))
print(ratio)



#x=open_hours[1][1]-open_hours[1][0]
#print(open_hours[1][1])
#print(x)