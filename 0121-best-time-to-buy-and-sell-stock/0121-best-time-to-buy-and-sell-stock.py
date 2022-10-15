class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        l , r = 0, 1
        while r < len(prices):
            #we need to buy it when it is valued less[ when the right pointer is much lesser]
            if prices[l] < prices[r]:
                Profit = prices[r] - prices[l]
                maxP = max(maxP, Profit)
            else:
                l=r    
            r += 1
        return maxP