
K = int(input())
rooms = list(map(int, input().split()))
Map = {}
for i in rooms:
    if i in Map:
        Map[i] += 1
    else:
        Map[i] = 1
for i in Map:
    if Map[i] != 1:
        continue
    else:
        print(i)
        
