class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        Hashset = set(nums)
        for i in range(1, len(nums)+1):   
            if i not in Hashset:
                return i
            else:
                continue
        return len(nums) + 1
        