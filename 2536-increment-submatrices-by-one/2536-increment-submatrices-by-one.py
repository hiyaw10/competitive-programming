class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        Row = n+1
        Col = n+1
        arr = [[0]*Row for _ in range(Col)]

        for q in queries:
            for i in range(q[0], q[-2]+1):
                arr[i][q[1]] += 1
                arr[i][(q[-1]+1)] -= 1
        ans = [[0]* n for _ in range(n)]
        for i in range(len(arr)):
            Sum = 0
            for j in range(len(arr[0])):
                Sum += arr[i][j]
                if i < n and j < n:
                    ans[i][j]=Sum

        return ans