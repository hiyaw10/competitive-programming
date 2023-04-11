class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        directions = [[-1,0], [0,-1], [1,0], [0,1]]
        
        row = len(image)
        col = len(image[0])
        if image[sr][sc] == color:
            return image
        
        def inBound(sr, sc):
            return 0 <= sr < row and 0 <= sc < col
        
        def dfs(sr, sc):
            prevColor = image[sr][sc] 
            image[sr][sc] = color
            
            for dr in directions:
                newRow = sr + dr[0]
                newCol = sc + dr[1]
                if inBound(newRow, newCol) and image[newRow][newCol] == prevColor:
                    dfs(newRow, newCol)
        dfs(sr, sc)
        return image
                    