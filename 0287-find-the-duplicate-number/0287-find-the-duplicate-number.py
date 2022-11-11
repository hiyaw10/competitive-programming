class Solution(object):
    def findDuplicate(self, nums):
        nums.sort()
        l, r = 0, 1
        while r < len(nums):
            if nums[l] == nums[r]:
                return nums[l]
            l += 1
            r += 1
        