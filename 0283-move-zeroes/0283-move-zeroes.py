'''
we are looking for an array with zeroes on the most left while the order of the remaining array is maintained.
in order to do that we need two pointers in order to not take extra memory space, so one pointer to scan through the List, while the other to do some more switches, it has a time complexitiy of O(n).
'''
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l = 0
        for r in range(len(nums)):
            if nums[r] != 0:
                nums[r], nums[l] = nums[l], nums[r]
                l += 1       
        return nums