class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
    
      
        curr_sum = sum(nums[:k])
        Sum = curr_sum
        
        for right in range(k, len(nums)):
            curr_sum += nums[right] - nums[right-k]
            Sum = max(curr_sum, Sum)
        return Sum/k
            