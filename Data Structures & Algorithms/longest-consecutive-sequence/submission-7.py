class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s1= set(nums)
        maxi=0
        for num in nums:
            if num-1 not in s1:
                s1.add(num)
                length=0
                while (num+length) in s1:
                    length+=1
                    maxi=max(length,maxi)
        return maxi