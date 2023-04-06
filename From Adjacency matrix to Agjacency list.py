
size = int(input())
adjMat = []
for _ in range(size):
    row = list(map(int, input().split()))
    adjMat.append(row)    
print(adjMat)


for row in range(len(adjMat)):
    ans = []
    for col in range(len(adjMat[0])):
        if adjMat[row][col] == 1:
            ans.append(col + 1)
    print(len(ans), *ans)
