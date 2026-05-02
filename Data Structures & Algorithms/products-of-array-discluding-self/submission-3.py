from math import prod
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lis=[]
        pdt= prod(nums)
        # for i in range(len(nums)):
            
        #     pref=prod(nums[0:i])
        #     suff=prod(nums[i+1:])
        #     lis.append(pref*suff)



    #     class Solution:
    # def productExceptSelf(self, nums: List[int]) -> List[int]:
    #     res=[1]*len(nums)
        
    #     prefix=1
    #     for i in range(len(nums)):
    #         res[i]=prefix
    #         prefix*=nums[i]

    #     suffix=1
    #     for i in range(len(nums)-1,-1,-1):
    #         res[i]*=suffix
    #         suffix*=nums[i]
    #     return res
        
        count=nums.count(0)
    
        if count>=2:
            for num in nums:
                lis.append(0)
        if count==0:
            for num in nums:
                v=pdt/num
                lis.append(int(v))
        if count==1:
            pdt1=1
            for i in nums:
                if i !=0:
                  pdt1=pdt1*i
                  
            for num in nums:
                if(num!=0):
                    lis.append(0)
                else:
                    lis.append(pdt1)
 
        return lis