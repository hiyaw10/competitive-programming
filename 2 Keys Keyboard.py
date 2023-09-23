class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0]*(n+1)
        dp[1] = 0
        if n >= 2:
            dp[2] = 2

        for i in range(3, n+1):
            dp[i] = i
            for j in range(2, int(i**0.5+1)):
                if i%j == 0:
                    dp[i] = dp[j]+dp[i/j]
                    break

        return dp[n]
        
