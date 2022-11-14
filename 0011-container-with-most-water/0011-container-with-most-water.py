class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        output = 0
        while l < r:
            Area = (min(height[r], height[l]) * (r - l))
            output = max(Area, output)
            if height[r] > height[l]:
                l += 1
            else:
                r -= 1
        return output
            