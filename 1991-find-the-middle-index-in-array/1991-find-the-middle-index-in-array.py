# class Solution:
#     def findMiddleIndex(self, nums: List[int]) -> int:
#         #sums = [ 0, list, 0]
#         sums = [0] * (len(nums)+2)
#         for i in range(len(nums)):
#             sums[i+1] = sums[i] + nums[i]
#         #We have generated a corresponding prefix sum of the given list of arrays.
#         if sums[-1] == sums[-3]:
#                 return len(nums) - 1
#         elif sums[-1] != sums[-3]:
#             for num in range(1, len(sums)+1):
#                 if sums[num] + sums[num - 1] == sums[-2]:
#                     return num-1
        
#         return -1
            
class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        leftSum = 0
        rightSum = sum(nums)
        
        for i in range(len(nums)):
            if leftSum == rightSum - nums[i]:
                return i
            leftSum = leftSum + nums[i]
            rightSum -= nums[i]
        return -1
