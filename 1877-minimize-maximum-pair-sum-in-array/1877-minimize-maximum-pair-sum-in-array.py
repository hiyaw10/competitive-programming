class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        i=0
        j=len(nums)-1
        m=0
        while i<=j:
            m=max(m,nums[i]+nums[j])
            i+=1
            j-=1
        return m