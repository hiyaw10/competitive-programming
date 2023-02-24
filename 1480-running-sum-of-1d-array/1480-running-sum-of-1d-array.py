class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        Sum = 0
        ans = []
        for i in nums:
            Sum += i
            ans.append(Sum)
        return ans