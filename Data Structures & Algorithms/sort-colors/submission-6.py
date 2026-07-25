class Solution:
   def sortColors(self, nums: List[int]) -> None:
      # zero= nums.count(0)
      # ones= nums.count(1)
      # one=zero+ones
      # twos= nums.count(2)
      # two=one+twos
      # for i in range(len(nums)):
      #    if i < zero:
      #       nums[i]= 0
      #    elif  i<one:
      #       nums[i]=1
      #    elif i<two:
      #       nums[i]=2
      l=0
      r=len(nums)-1
      mid=0
      while(mid<=r):
         if nums[mid]==0:
            nums[l],nums[mid]=nums[mid],nums[l]
            l=l+1
            mid+=1
         elif nums[mid]==1:
            mid+=1
         else:
            nums[r],nums[mid]=nums[mid],nums[r]
            r=r-1
            
         



        