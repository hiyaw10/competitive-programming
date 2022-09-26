class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        r=[]
        d={}
        n=sorted(nums)
        for i in range(len(n)):
            if n[i] not in d:
                 d[n[i]]=i
        for i in nums:
            r.append(d[i])
        return r