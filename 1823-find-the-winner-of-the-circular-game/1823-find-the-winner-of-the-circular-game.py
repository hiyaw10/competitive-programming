class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        nums = list(range(1, n+1))
        print(nums)
        
        i = 0
        while len(nums) > 1:
            i = (i + k - 1) % len(nums)
            nums.pop(i)
        return sum(nums)
            
        