class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        total_sum = sum(nums)
        cur_sum = 0
        
        for i,num in enumerate(nums):
            if total_sum-cur_sum*2== num:
                return i
            
            #update the cur_sum
            cur_sum += num
            
        return -1