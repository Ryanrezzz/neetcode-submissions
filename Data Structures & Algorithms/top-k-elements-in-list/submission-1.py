class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        spare={}
        for num in nums:
            if num in spare:
                spare[num]+=1
            else:
                spare[num]=1
        lst=sorted(spare,key=spare.get,reverse=True)

            
        
                
        return lst[0:k]