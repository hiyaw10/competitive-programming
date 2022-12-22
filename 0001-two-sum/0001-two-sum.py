class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        we need a hashmap
        we check for the difference of the target and the current number in the library
        then we are good to go
        """
        hashMap = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in hashMap:
                return [hashMap[diff], i]
            else:
                hashMap[n] = i