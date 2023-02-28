class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        Sum = 0
        dic = {}
        dic[0] = 1
        for i in range(len(nums)):
            Sum += nums[i]
            if Sum-k in dic:
                count += dic[Sum-k]
            dic[Sum] = dic.get(Sum, 0)+1
        return count