#Brute force
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        diff = 0
        for i in range(len(prices)):
            for j in range(1,len(prices)):
                if (prices[j]-prices[i]) > diff and j>i :
                    print(i,j)
                    diff = prices[j] - prices[i]
        return diff
            
