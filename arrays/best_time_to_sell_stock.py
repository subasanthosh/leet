class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit = 0

        for i in prices:
            if buy > i:
                buy = i
            profit = max(i-buy,profit)

        return profit