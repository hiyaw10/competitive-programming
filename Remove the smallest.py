N = int(input())
for _ in range(N):
    n = int(input())
    List = list(map(int, input().split()))
    List.sort()
    for i in range(1, n):
        if List[i] - List[i-1] > 1:
            print("NO")
            break 
    else:
        print("YES")
