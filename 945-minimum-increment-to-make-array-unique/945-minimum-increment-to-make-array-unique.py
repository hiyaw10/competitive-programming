class Solution:
    
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        for i in range(1, len(nums)):
            pre = nums[i-1]
            cur = nums[i]
            if pre >= cur:
                res += pre-cur+1 # recording the no of changes
                nums[i] = pre + 1 # increasing the (i-1)th value by 1 and assigning it to ith value
        return res   