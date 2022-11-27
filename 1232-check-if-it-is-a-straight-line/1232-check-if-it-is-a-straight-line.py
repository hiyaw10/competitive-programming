class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x0, y0 = coordinates[0]
        x1, y1 = coordinates[1]
        chanY = y1 - y0
        chanX = x1 - x0
        xp = chanX*y0 - chanY*x0    # See analysis below

        for x, y in coordinates:
            if chanX*y - chanY*x != xp:
                return False
        else:
            return True