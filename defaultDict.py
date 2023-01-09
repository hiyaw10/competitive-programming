from collections import defaultdict
A, B = map(int,input().split())
index = defaultdict(list)

for i in range(1, A+1):
    index[input()].append(i)

N = []
for i in range(B):
    N.append(input())

for char in N:
    if char in index.keys():
        print(" ".join(map(str, index[char])))
    else:
        print(-1)
