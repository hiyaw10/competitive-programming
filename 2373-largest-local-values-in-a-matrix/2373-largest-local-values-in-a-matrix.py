class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid) - 2
       
        output = maxLocal = [[0 for _ in range(n)] for _ in range(n)]
        
        for i in range(n):
            for j in range(n):
                Max = max(grid[i][j:j+3])
                Max2 = max(grid[i+1][j:j+3])
                Max3 = max(grid[i+2][j:j+3])
                output[i][j] = max(Max, Max2, Max3)
        return output
        