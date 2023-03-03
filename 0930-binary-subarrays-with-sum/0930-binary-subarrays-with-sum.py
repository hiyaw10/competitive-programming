class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        runningSum = {0:1}
        
        Sum = 0
        ans = 0
        for i in nums:
            Sum += i
            
            diff = Sum - goal
            
            if diff in runningSum:
                ans += runningSum[diff]
            runningSum[Sum] = 1 + runningSum.get(Sum, 0)
        return ans