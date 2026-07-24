class Solution:
   def majorityElement(self, nums: List[int]) -> int:
      # n=len(nums)/2
      # hashmap={}
      # for value in nums:
      #    if value in hashmap:
      #       hashmap[value]+=1
      #    else:
      #       hashmap[value]=1

      # for key,value in hashmap.items():
      #    if value>n:
      #       return key

      n= len(nums)/2
      nums.sort()
      count=1
      j=1
      c=1
      if len(nums)== 1:
         return nums[0]
      for i in range(len(nums)):
         if nums[i]==nums[j]:
            c+=1
            count= max(count,c)
            j=j+1 
            if count>n:
               return nums[i]
               
         
