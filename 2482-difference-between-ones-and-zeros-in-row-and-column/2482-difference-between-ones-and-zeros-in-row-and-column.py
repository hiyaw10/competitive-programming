class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        
        m, n = len(grid), len(grid[0])
        row = [0] * m  
        col = [0] * n
        
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                col[j] += grid[i][j]
                row[i] += grid[i][j]
        ans = []
        for i in range(len(grid)):
            temp = []
            for j in range(len(grid[0])):
                temp.append(row[i] + col[j] - (n - row[i]) - (m - col[j]))
            ans.append(temp)
        return ans