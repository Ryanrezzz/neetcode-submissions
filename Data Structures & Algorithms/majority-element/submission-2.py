class Solution:
   def majorityElement(self, nums: List[int]) -> int:
      n=len(nums)/2
      hashmap={}
      for value in nums:
         if value in hashmap:
            hashmap[value]+=1
         else:
            hashmap[value]=1

      for key,value in hashmap.items():
         if value>n:
            return key
         
