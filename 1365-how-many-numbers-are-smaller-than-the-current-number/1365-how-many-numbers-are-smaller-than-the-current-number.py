class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        Sorted = sorted(nums)
        hashmap = {}
        ans = []
        for i in range(len(Sorted)):
            if Sorted[i] not in hashmap:
                hashmap[Sorted[i]] = i
        for i in range(len(nums)):
            ans.append(hashmap[nums[i]])
        return ans
            
        