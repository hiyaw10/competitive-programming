class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
    
      
        curr_sum = sum(nums[:k])
        Sum = curr_sum
        left = 0
        for right in range(k, len(nums)):
            curr_sum += nums[right] - nums[left]
            left += 1
            Sum = max(curr_sum, Sum)
        return Sum/k
            