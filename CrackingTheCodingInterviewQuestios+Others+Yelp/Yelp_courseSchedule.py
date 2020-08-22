n = 2
#prereq = [[1,0],[0,1]]
prereq = [[5,8],[3,5],[1,9],[4,5],[0,2],[1,9],[7,8],[4,9]]

print(prereq[3][1])
print(prereq[3][0])
print(sorted(prereq))

print(len(prereq))

for i in range(len(prereq)):
    print("1st for")
    print(i)
    for j in range(i+1,len(prereq)):
        print(j)
        if prereq[i][0] == prereq[j][1]:
            print("cant take course")