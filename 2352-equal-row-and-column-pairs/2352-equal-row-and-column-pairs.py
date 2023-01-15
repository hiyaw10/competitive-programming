class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        hashmap = {}
        for i in range(len(grid)):
            temp = []
            for j in range(len(grid[0])):
                temp.append(str(grid[i][j]))
            x = ",".join(temp)
            if x in hashmap:
                hashmap[x] += 1
            else:
                hashmap[x] = 1
        
        count = 0
        for i in range(len(grid[0])):
            Temp = []
        
            for j in range(len(grid)):
                Temp.append(str(grid[j][i]))
            y = ",".join(Temp)
            
            if y in hashmap:
                count += hashmap[y]
        return count
                