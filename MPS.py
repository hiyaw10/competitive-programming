class Solution(object):
    def maxProduct(self, nums):
        pre = suff = 1
        res = nums[0]
        for i in range(len(nums)):
            l = len(nums) - i - 1
            if pre == 0:
                pre = 1
            if suff == 0:
                suff = 1
            pre = pre * nums[i]
            suff = suff * nums[l]
            res = max(res, max(pre, suff))
        return res  
        
        
        
        
        
        
        
        
        
        
        
