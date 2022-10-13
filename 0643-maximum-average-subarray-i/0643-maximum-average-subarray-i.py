# class Solution:
#     def findMaxAverage(self, nums: List[int], k: int) -> float:
#         l, r = 0, 0 
#         maxAverage = 0
#         summ = 0
#         while r < len(nums):
#             if r - l != k:
#                 for i in range(k):
#                     summ = summ + nums[r]
#                 maxAverage = max(maxAverage, summ)
#             else:
#                 l = r
#             r+=1
#         return (maxAverage/k)
    
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr = 0
        for i in range(k):
            curr+=nums[i]
            maxx = curr
        for i in range(k,len(nums)):
            curr += nums[i] - nums[i-k]
            if curr>maxx:
                maxx = curr
        return maxx/k       