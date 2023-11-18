class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        
        p = coordinates
        n = len(p)
        if n == 2:
            return True
        
        x0, y0 = p[0]
        x1, y1 = p[1]

        for i in range(2, n):
            x, y = p[i]
            if (y1 - y0) * (x - x1) != (y - y1) * (x1 - x0):
                return False
        return True