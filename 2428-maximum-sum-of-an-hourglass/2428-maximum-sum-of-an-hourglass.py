class Solution:
    def maxSum(self, x: List[List[int]]) -> int:
        
        
        Max = 0
        
        m = len(x)
        n = len(x[0])
        for i in range(m-2):
            for j in range(n-2):
                mSum =0
                for k in range(j, j+3):
                    mSum +=x[i][k]
                for k in range(j, j+3):
                    mSum +=x[i+2][k]
                
                mSum += x[i+1][j+1]
                if Max < mSum:
                    Max = mSum
        return Max