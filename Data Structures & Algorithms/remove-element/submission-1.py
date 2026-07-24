class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
      # for i in range(len(nums)-1,-1,-1):
      #    if nums[i] == val:
      #       nums.pop(i)
            
      # return len(nums)

      # j=0
      j=0

      for i in range(len(nums)):
         if nums[i]!=val:
            nums[j]=nums[i]
            j+=1
      return j