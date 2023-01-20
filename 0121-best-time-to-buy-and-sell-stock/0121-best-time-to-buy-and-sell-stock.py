class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        Max = 0
        
        l, r = 0, 1
        
        while r < len(prices):
            if prices[l] >=prices[r]:
                l = r
            else:
                diff = prices[r] - prices[l]
                Max = max(diff, Max)
            r += 1
        return Max