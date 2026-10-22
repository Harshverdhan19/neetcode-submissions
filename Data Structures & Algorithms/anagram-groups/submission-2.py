class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for word in strs:
            count = [0] * 26

            for c in word:
                count[ord(c) - ord('a')] += 1 # a=0, b = 1, c = 2 ....

            key = tuple(count) # lists cant be keys, tuple can
            if key not in groups:
                groups[key] = []

            groups[key].append(word)

        return list(groups.values()) 


        