class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        n = len(prices)
        dp = [[0]*(n+1) for _ in range(3)]
        for i in range(1, 3):
            max_diff = -prices[0]
            for j in range(1, n):
                dp[i][j+1] = max(dp[i][j], prices[j] + max_diff)
                max_diff = max(max_diff, dp[i - 1][j] - prices[j])

        
        return dp[2][n]

