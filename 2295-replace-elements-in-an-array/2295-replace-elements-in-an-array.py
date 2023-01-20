class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        hashmap = {}
        for i, n in enumerate(nums):
            hashmap[n] = i
        for x, y in operations:
            if x in hashmap:
                nums[hashmap[x]] = y
                re = hashmap[x]
                del hashmap[x]
                hashmap[y] = re
        return nums
                
        