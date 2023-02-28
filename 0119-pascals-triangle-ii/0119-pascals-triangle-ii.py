class Solution:
    def getRow(self, n: int) -> List[int]:
        if n == 0:
            return [1]
        if n == 1:
            return [1, 1]
        arr = self.getRow(n-1)
        currArr = [1] * (n+1)
        
        for i in range(1, n):
            currArr[i] = arr[i-1] + arr[i]
        return currArr
        