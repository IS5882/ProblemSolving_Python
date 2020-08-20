def maxTime(s):

    print(s)
    minTime=""
    for i in range(len(s)):
        if s[i]!="?":
            minTime+=s[i]
            continue

        if i==0: #hour Slot
            if s[1]=="?" or s[1]=="1" or s[1]=="2" or s[1]=="3":
                minTime+="2"
            else:
                minTime+="1"

        elif i==1: #hour slot2
            minTime+="3" if minTime[0]=="2" else "9"

        elif i==3: #min1
            minTime +="5"

        elif i==4:
            minTime += "9"

    print('new S',minTime)
    return minTime


assert (maxTime("?4:5?")== "14:59")
assert (maxTime("23:5?")== "23:59")
assert (maxTime("2?:22")== "23:22")
assert (maxTime("0?:??")== "09:59")
assert (maxTime("??:??")== "23:59")