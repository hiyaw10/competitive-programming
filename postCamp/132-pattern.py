class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = [] 
        Min = nums[0]
        
        for n in nums:
            while stack and stack[-1][0] < n:
                stack.pop()
            if stack and n < stack[-1][0] and n > stack[-1][1]:
                return True
            stack.append([n, Min])
            Min = min(Min, n)
        return False