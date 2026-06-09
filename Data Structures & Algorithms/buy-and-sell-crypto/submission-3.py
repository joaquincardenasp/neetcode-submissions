class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        j = 0
        lowest = prices[0]
        maxProfit = 0
        while j < len(prices):
            if prices[j] < lowest:
                lowest = prices[j]
            else:
                profit = prices[j] - lowest
            if maxProfit < profit:
                maxProfit = profit
            j+=1
        return maxProfit
            