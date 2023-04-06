

n = int(input())
adjMat = []
for _ in range(n):
    r = list(map(int, input().split()))
    adjMat.append(r)

source = []
sink = []
for row in range(len(adjMat)):
    Bool = True
    for col in range(len(adjMat[0])):
        if adjMat[row][col] == 1:
            Bool = False
    if Bool: sink.append(row+1)

for co in range(len(adjMat[0])):
    B = True
    for ro in range(len(adjMat)):
        if adjMat[ro][co] == 1:
            B = False
    if B: source.append(co+1)

print(len(source), *source)
print(len(sink), *sink)





