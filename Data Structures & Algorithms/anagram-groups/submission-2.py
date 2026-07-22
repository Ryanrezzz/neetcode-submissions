class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        spare={}
        for word in strs:
            sort_word="".join(sorted(word))
            if sort_word in spare:
                spare[sort_word].append(word)
            else:
                spare[sort_word]=[word]
            
        return list(spare.values())

