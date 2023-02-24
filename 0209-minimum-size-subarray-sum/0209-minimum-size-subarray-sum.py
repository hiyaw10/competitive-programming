class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        curr_sum, res = 0, float("inf")
        for right in range(len(nums)):
            curr_sum += nums[right]
            while target <= curr_sum:
                res = min(right - left + 1, res)
                curr_sum -= nums[left]
                left += 1
        
        if res == float("inf"):
            return 0
        return res