class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        l, r = 0, k-1 #how our window size has to be!
        res = float("inf") #we just intialized to the maximum possible value
        while r < len(nums):
            res = min(res, nums[r]-nums[l])
            l, r = l+1, r+1
        return res