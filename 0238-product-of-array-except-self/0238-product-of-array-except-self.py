class Solution:

    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n=len(nums)
        output=[0]*n

        prev=1
        for i in range(n):
            output[i]=prev
            prev*=nums[i]

        post=1
        for i in range(1,n+1):
            output[-i]*=post
            post*=nums[-i]

        return output
