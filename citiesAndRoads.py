size = int(input())
adjMat = []


for _ in range(size):
    row = list(map(int, input().split()))
    adjMat.append(row)
ans = 0
for row in adjMat:
    for j in row:
        if j == 1:
            ans += 1
    
print(ans//2)
