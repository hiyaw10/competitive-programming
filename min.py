class Solution:
    def minOperations(self, nums: List[int]) -> int:
        full_l = len(nums) - 1
        nums = list(set(nums))
        nums.sort()
        l = len(nums) - 1
        max = 0
        for i in range(l):
            right_indx = bisect.bisect(nums, nums[i] + full_l) - 1
            seq_len = right_indx - i
            if (seq_len > max) and (seq_len > 0):
                max = seq_len
        
        return full_l - max
