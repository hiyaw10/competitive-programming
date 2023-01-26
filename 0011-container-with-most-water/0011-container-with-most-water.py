class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        ans = 0
        while l < r:
            Area = min(height[r], height[l]) * (r - l)
            if height[r] >= height[l]:
                ans = max(Area, ans)
                l += 1
            else:
                ans = max(Area, ans)
                r -= 1
        return ans