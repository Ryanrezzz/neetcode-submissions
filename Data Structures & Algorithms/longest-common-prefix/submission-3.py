class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
      # prefix=strs[0]

      # for i in range(1, len(strs)):
      #    j=0
      #    while(j<min(len(prefix),len(strs[i]))):
      #       if prefix[j]!=strs[i][j]:
      #          break;
      #       j=j+1
      #    prefix= prefix[:j]
      # return prefix
      strs=sorted(strs)
      first= strs[0]
      last= strs[-1]
      j=0
      while(j<len(first)and j<len(last) and first[j]==last[j]):
         j+=1
      return first[:j]        