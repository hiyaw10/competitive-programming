# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         List = []
#         for i in range(0, len(nums) - 1):
#             for j in range(0, len(nums)-i-1):
#                 if nums[j+1] > nums[j]:
#                     nums[j+1], nums[j] = nums[j], nums[j+1]
#             if nums[j]+1 != nums[j+1]:
#                 List.append(nums[j])
#             if nums[j] == len(nums):
#                 return nums[j] + 1
        
#         return nums[j] - 1
class Solution(object):
    def missingNumber(self, nums):
        l=len(nums)
        m=min(nums)
        for i in range(m,l+1,1):
            if(i not in nums):
                return i
        return 0