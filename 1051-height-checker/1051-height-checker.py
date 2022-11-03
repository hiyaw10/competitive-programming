class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sort_heights = sorted(heights)
        return sum([0 if heights[i] == sort_heights[i] else 1 for i in range(len(heights))])
        