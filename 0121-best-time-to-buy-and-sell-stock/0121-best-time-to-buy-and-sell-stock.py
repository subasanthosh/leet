class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prof = 0
        buy = prices[0]
        for i in prices:
            if buy>i:
                buy = i
            prof = max(prof,i-buy)
        return prof