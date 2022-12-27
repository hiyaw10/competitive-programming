class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        min1 = float('inf')
        res = -1
        for i in range(len(points)):
            if points[i][0]==x or points[i][1]==y:
                diff = abs(points[i][0]-x)+abs(points[i][1]-y)
                if diff<min1:
                    res = i
                    min1 = diff
        return res
        