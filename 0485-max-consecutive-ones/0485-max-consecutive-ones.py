class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        l=r = 0
        output = 0
        while r < len(nums):
            if nums[r] == 1 and nums[l] == 1:
                output = max(output, r-l+1)
                r += 1
            else:
                r += 1
                l = r
        return output