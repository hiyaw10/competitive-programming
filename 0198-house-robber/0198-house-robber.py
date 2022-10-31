class Solution:
    def rob(self, nums: List[int]) -> int:
		# if list length <= 2, choose max number
        if len(nums) <= 2:
            return max(nums)
        nums[1] = max(nums[0:2])
        for i in range(2,len(nums)):
            nums[i] = max(nums[i-1], nums[i-2] + nums[i])  # equal to max of [i-2] + [i] and [i-1]
        
		# return the last value / max value of whole list
        return nums[-1]