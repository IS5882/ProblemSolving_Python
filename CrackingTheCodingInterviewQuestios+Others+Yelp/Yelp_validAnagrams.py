s=("ckat")
#t=("cinac")


class Solution:
    """
    @param s: The first string
    @param t: The second string
    @return: true or false
    """

    def anagram(self, s, t):
        return sorted(s) == sorted(t)
"""



    def anagram(self, s, t):
        if (len(s) != len(t)):
            return (False)
        for i in s:
            if i not in t:
                return (False)
            else:
                t.replace(i, "")
        return (True)

"""
