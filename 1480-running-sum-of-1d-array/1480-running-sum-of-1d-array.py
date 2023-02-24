class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        Sum = 0
        ans = [0] * len(nums)
        l = 0
        for i in nums:
            Sum += i
            ans[l] = Sum
            l += 1
        return ans