class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i=0
        max_prof=0
        buy=0
        for j in range(len(prices)):
            buy=prices[i]
            if buy>prices[j]:
                i=j
                buy=prices[i]
            else:
                sell=prices[j]-buy
                max_prof=max(max_prof,sell)
        return max_prof


