class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #keep our left as low as possible while trying to find our right as high as possible
        
        left, right = 0, 1
        maxProfit = 0
        
        while right < len(prices):
            diff = prices[right] - prices[left] #we want to maximize this
            if diff > 0:
                maxProfit = max(maxProfit, diff)
            else:
                left = right
            right += 1
            
        return maxProfit