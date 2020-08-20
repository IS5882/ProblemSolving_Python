import collections


class Solution:
    def numSplits(self, s: str) -> int:
        myS1 = collections.Counter()  # s1 is now empty
        myS2 = collections.Counter(s)  # s2 is now has all string
        ways = 0  # when len of myS1= len of myS2 --> ways+=1

        for letter in s:
            myS1[letter] += 1
            myS2[letter] -= 1

            if myS2[letter] == 0:
                myS2.pop(letter)

            if len(myS1) == len(myS2):
                ways += 1  # ways1
        return ways

