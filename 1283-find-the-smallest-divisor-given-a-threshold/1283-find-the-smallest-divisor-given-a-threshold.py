class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        #boundaries
        l, r = 0, max(nums) + 1
        
        while l+1 < r:
            mid = l + (r-l)//2
            ans = 0
            
            for i in nums:
                ans += ceil(i/mid)
            if ans <= threshold:
                r = mid 
            else:
                l = mid
        return r