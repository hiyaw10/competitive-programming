class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        charSet = set()
        for i in range(len(nums)):
            if nums[i] in charSet:
                return True
            else:
                charSet.add(nums[i])
        return False
        