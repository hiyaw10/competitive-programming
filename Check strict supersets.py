# Enter your code here. Read input from STDIN. Print output to STDOUT
A = list(map (int, input().split()))
n = int(input())
x = 0
for i in range(n):
    List = list(map(int, input().split()))
    for j in List:
        if j not in A:
            x += 1
        else:
            continue
print(x == 0) 
