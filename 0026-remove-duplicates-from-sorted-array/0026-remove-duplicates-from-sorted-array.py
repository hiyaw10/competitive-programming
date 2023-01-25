class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l, r = 1, 0
        for r in range(1, len(nums)):
            if nums[r-1] != nums[r]:
                nums[l] = nums[r]
                l += 1
        return l
        