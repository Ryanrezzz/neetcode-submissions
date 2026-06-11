class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        spare = {}
        for word in strs:
            sort_ver= "".join(sorted(word))
            if sort_ver in spare:
                spare[sort_ver].append(word)
            else:
                spare[sort_ver]=[word]
            
        return list(spare.values())

