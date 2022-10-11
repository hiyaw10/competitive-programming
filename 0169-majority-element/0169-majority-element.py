class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c=1
        t=nums[0]
        n=len(nums)
        for i in range(1,n):
            if c==0:
                t=nums[i]
                c=1
            else:
                if nums[i]==t:
                    c+=1
                else:
                    c-=1
        return t