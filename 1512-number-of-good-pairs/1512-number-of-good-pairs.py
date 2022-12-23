class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counter = Counter(nums)
        res = 0
        
        for n in counter.values():
            if n > 1:
                res += (n-1) * (n)// 2
        return res
        