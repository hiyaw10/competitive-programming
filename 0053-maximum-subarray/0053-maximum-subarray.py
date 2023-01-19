class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        Sum = 0
        
        for n in nums:
            if Sum < 0:
                Sum = 0
            Sum += n    
            res = max(res, Sum)
        return res
        