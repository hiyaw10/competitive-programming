class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # method1: prefix sum
        prefixCount = {0:1}
        res = 0
        oddCount = 0
        for i in range(len(nums)):
            oddCount = oddCount + (1 if nums[i]%2 == 1 else 0)
            residual = oddCount - k
            res += prefixCount.get(residual,0)
            prefixCount[oddCount] = 1 + prefixCount.get(oddCount,0)
        return res