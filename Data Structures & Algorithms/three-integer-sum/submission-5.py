class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        hashmap=set()
        nums=sorted(nums)
        for i in range(len(nums)):
            left=i+1
            right=len(nums)-1
            while(left<right):

                total = nums[i] + nums[left] + nums[right]
                if(total==0):
                    triplet=[nums[i],nums[left],nums[right]]
                    hashmap.add(tuple(triplet))
                    left+=1
                    right-=1
                elif total<0:
                    left+=1
                else:
                    right-=1
        
        return [list(d) for d in hashmap]
         
            
        
