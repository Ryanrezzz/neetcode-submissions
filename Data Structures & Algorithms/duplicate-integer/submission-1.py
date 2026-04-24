class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a =True
        b=False

        if len(nums) != len(set(nums)):
            return a
        else:
            return b