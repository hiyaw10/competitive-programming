class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        ans, curr_sum = 0,0
        while len(prices) > right:
            if prices[left] > prices[right]:
                left = right
            else:
                curr_sum = max(curr_sum, prices[right] - prices[left])
            right += 1
            ans = max(ans, curr_sum)
        return ans