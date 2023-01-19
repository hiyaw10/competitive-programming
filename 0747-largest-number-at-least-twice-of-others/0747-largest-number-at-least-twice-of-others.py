class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        Max1 = max(nums)
        ans = 0
        for i in range(len(nums)):
            if nums[i] == Max1:
                ans = i
        nums.remove(Max1)
        if (2*max(nums)) <= Max1:
            return ans
        return -1
        