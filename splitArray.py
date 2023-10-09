class Solution(object):
    def maxSubarrays(self, nums):
        score, res = -1, 1
        for i in nums:
            score &= i
            if score == 0:
                score = -1
                res += 1
        return 1 if res == 1 else res - 1
        
