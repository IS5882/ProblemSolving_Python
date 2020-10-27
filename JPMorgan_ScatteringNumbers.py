#https://leetcode.com/discuss/interview-question/773647/JPMorgan-or-Online-Assessment

def scatteringNo(start,end):

    def scrolling(n):
        seen=set()
        moveSteps=0

        while True:
            moveSteps=(moveSteps+int(n[moveSteps]))%len(n)

            if len(seen)==len(n):
                return True
            if n[moveSteps] in seen:
                return False
            seen.add(n[moveSteps])

        #nextMove=(moveSteps+int(n[moveSteps]))%len(n)
        print('seen',seen)
        #return nextMove==0 and len(seen)==len(n)

    res=[]
    for n in range(start,end+1):
        s=str(n)
        if len(set(s))<len(s): #ie:a digit is repeated twice so no need to check
            continue
        if scrolling(str(n)):
            res.append(n)
    return res

print(scatteringNo(100,500))
print(scatteringNo(6231,6231))