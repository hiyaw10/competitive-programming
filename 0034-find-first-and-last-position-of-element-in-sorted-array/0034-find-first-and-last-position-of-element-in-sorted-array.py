class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low, high = -1 , len(nums)
        
        while low + 1 < high:
            mid = (low + high)//2
            if nums[mid] >= target:
                high = mid
            else:
                low = mid
        l, r = -1, len(nums)        
        while l + 1 < r:
            mid2 = (l + r)//2
            
            if nums[mid2] > target:
                r = mid2
            else:
                l = mid2
        
        if not nums or nums[l] != target:
            return [-1, -1]
        return [high, l]
        
            