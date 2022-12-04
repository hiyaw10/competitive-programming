class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = sum(nums)
        minindex = 0
        minn = 10 ** 20
        
        for i in range(n):
            left += nums[i]
            right -= nums[i]
            
            if i + 1 == n:
                r = abs(left//(i + 1))
            else:
                r = abs(left//(i+1) - right // (n - i - 1))
            if r < minn:
                minn = r
                minindex = i
        return minindex
                