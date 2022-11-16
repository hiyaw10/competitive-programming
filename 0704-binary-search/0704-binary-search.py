class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l, r = 0, len(nums)
        
        if target in nums:
            while True:
                m = (l + r) // 2
                if nums[m] > target:
                    r = m - 1
                elif nums[m] < target:
                    l = m + 1
                else:
                    return m
        else:
            return -1

            