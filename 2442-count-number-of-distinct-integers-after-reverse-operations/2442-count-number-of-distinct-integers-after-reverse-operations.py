class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        x = [int(str(n)[::-1]) for n in nums]
        array = nums + x
        return len(set(array))