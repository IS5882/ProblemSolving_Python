import collections
def solve(A, B):

    #A="abcd,aabc,bd"

    #B="aaa,aa"


    wordsA = A.split(",")
    wordsB = B.split(",")

    print('wordsA',wordsA)
    #loop on smaller one
    #if len(wordsA)>len(wordsB):
     #   wordsA,wordsB=wordsB,wordsA


    res=[]

    for b in wordsB: #abcd
        print('b:',b)
        countSmaller=0
        print('min b',min(b))
        myB=b.count(min(b))
        print('count of min',myB)
        for a in wordsA: #aaa
            print('a:',a)
            print('min a', min(a))
            myA = a.count(min(a))
            print('count of min', myB)
            if myA<myB:
                countSmaller+=1
            print('countSmaller is',countSmaller)

        res.append(countSmaller)

    print('res',res)
    return res




assert (solve("abcd,aabc,bd","aaa,aa")==[3,2])
assert (solve("abcd","aaa")==[1])
assert (solve("a","bb")==[1])

"""    for b in wordsB: #abcd
        print('b:',b)
        countSmaller=0
        myB=collections.Counter(b)
        for a in wordsA: #aaa
            print('a:',a)
            #if b[0] ==a[0]
            myA=collections.Counter(a) #
            if b[0] == a[0]: #a
                if myA[a[0]]<myB[b[0]]: #1<3
                    countSmaller+=1
            elif myA[a[0]]<myB[b[0]]:
                countSmaller+=1
            print('countSmaller is',countSmaller)

        res.append(countSmaller)
"""