class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s1= set(nums)
        maxi=0
        for k in nums:
            if k-1 not in s1:
                s1.add(k)
                length=0
                while (k+length) in s1:
                    length+=1
                    maxi=max(length,maxi)

        return maxi


