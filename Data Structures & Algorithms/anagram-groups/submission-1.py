class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {} 

        for word in strs: #eat
            key = "".join(sorted(word)) #act becomes = "aet". sort the words into a string instead of list 

            if key not in groups: # key "act" not in groups
                groups[key] = [] # add it in the groups dict

            groups[key].append(word) #if it is already added

        return list(groups.values()) 
        