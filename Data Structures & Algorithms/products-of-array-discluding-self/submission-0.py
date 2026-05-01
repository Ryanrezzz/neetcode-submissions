from math import prod
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lis=[]
        for i in range(len(nums)):
            
            pref=prod(nums[0:i])
            suff=prod(nums[i+1:])
            lis.append(pref*suff)
        
        return lis