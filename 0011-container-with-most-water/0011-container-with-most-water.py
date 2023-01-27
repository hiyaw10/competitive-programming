class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxA = 0
        l, r = 0, len(heights) - 1
        
        while l < r:
            Area = min(heights[r], heights[l]) * (r - l)
            if heights[l] >= heights[r]:
                r -= 1
                maxA = max(maxA, Area)
            else:
                maxA = max(maxA, Area)
                l += 1
        return maxA