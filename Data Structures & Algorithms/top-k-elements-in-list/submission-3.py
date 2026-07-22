class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        spare={}
        for value in nums:
            if value in spare:
                spare[value]+=1
            else:
                spare[value]=1
            sor_arr= sorted(spare, key=spare.get, reverse=True)
        return sor_arr[0:k]



