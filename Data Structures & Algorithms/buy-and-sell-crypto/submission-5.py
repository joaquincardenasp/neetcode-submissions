class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        highest = 0
        profit = 0
        for j in range(1,len(prices)):
            if prices[j]<prices[i]:
                i=j
            else:
                profit = prices[j]-prices[i]
            if highest < profit:
                highest = profit
        return highest
