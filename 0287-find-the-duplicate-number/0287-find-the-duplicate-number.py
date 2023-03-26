class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        res = [0] * len(nums)
        
        for num in nums:
            if res[num-1] != 0:
                return num
            res[num-1] = num
    