class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ls = list(s)
        ls.extend(list(t))
        for i in range(len(ls)):
            x = ls.count(ls[i])
            if x%2 != 0:
                return ls[i]
