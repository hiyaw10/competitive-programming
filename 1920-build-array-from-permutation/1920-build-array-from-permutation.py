class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        res = []
        
        for i in range(len(nums)):
            value = nums[nums[i]]
            res.append(value)
        return res