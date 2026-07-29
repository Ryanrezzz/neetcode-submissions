class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        #Boyer–Moore Voting Algorithm.
        candidate1=None
        cnt1=0
        candidate2=None
        cnt2=0
        for num in nums:
            if candidate1==num:
                cnt1+=1
            elif candidate2==num:
                cnt2+=1
            elif cnt1==0:
                candidate1=num
                cnt1+=1
            elif cnt2==0:
                candidate2=num
                cnt2+=1
            else:
                cnt1-=1
                cnt2-=1
        c1=0
        c2=0
        n=len(nums)//3
        
        for num in nums:
            if candidate1 ==num :
                c1+=1
            if candidate2==num:
                c2+=1
        ans=[]
        if c1>n:
            ans.append(candidate1)
        if c2>n:
            ans.append(candidate2)
        return ans
    

         

            