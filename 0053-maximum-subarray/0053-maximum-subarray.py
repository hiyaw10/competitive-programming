class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        Sum = 0
        res = nums[0]
        
        for i in nums:
            if Sum < 0:
                Sum = 0
            Sum += i
            res = max(res, Sum)
        return res