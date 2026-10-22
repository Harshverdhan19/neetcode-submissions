class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        CountT = {}
        CountS = {}

        for i in range(len(s)):
            CountS[s[i]] = CountS.get(s[i], 0) + 1
            CountT[t[i]] = CountT.get(t[i], 0) + 1

            
            
        return CountT == CountS