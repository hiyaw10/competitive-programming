class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        l, r = 0, 1
        while r < len(prices):
            if prices[r] > prices[l]:
                difference = prices[r] - prices[l]
                maxP = max(difference, maxP)
            else:
                l = r
            r += 1
        return maxP