#https://leetcode.com/discuss/interview-question/797724/Google-Online-Challenge-Intern-2021-(Coding-Questions-%3A-2-or-Time-%3A-60-mins)

def goodSubString(s):

    if not s:
        return 0
    subStrings=0
    flagRev=2 #0 for increse, 1 for Dec, 2 for startMode

    for i in range(len(s)-1):

        if s[i]>s[i+1]:

            if flagRev==1:
                   subStrings = subStrings+1
                   flagRev=2
            else:
                flagRev = 0

        elif s[i]<s[i+1]:

            if flagRev==0:
                 subStrings=subStrings+1
                 flagRev=2
            else:
               flagRev = 1

    return subStrings+1

assert (goodSubString("abcdcba")==2)
assert (goodSubString("xyzabc")==2)
assert (goodSubString("xyza")==2)
assert (goodSubString("abc")==1)
assert (goodSubString("zabc")==2)
assert (goodSubString("zda")==1)
assert (goodSubString("zab")==2)


"""Question 1:

A string is called good if all its characters form a monotonous sequence(non-increasing or non-decreasing).
You are given a string S consisting of lower case Engligh alphabets. Determine the minimum numbers of contiguous substrings in which S must be broken such that each substring is good.

Note : A substring is a contiguous sequence of characters in a string.

Input format:
The first and only line contains string S.

Output format:
Print an integer denoting the required answer

Constraints:
1 <= len(S) <= 10^5

All characters in the String S will be lower case English Alphabets.

Sample Input : abcdcba
Sample Output : 2"""