class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        i, j = 0, len(nums)-1
        res = 0
        while(i<j):
            summ = nums[i]+nums[j]
            if(summ == k):
                i+=1
                j-=1
                res+=1
            elif(summ < k):
                i+=1
            else:
                j-=1
        return res