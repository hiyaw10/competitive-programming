class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums) < 2:
            return 0
        ans = 0
        for i in range(len(nums)-1):
            diff = -nums[i] + nums[i+1]
            ans = max(ans, diff)
        return ans