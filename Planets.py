n = int(input())
for i in range(n):
    x = 0
    a, b = map(int, input().split())
    K = list(map(int, input().split()))
    Z = {}
    for i in K:
        if i in Z:
            Z[i] += 1
        else:
            Z[i] = 1
    
    for orbit, freq in Z.items():
        if freq > b:
            x += b
        else:
            x += freq
    print(x)
