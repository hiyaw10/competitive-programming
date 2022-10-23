class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = 100000
        
        for i in range(len(nums) - k + 1):
            arr = nums[i:i + k]
            res = min(res, arr[-1] - arr[0])
            
        return res