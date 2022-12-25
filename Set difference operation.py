# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())
E = list(map(int, input().split()))
G = int(input())
F = list(map(int, input().split()))
count = 0
for i in E:
    if i in F:
        continue
    else:
        count += 1
print(count)
