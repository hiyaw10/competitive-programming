from collections import deque
def piling(d):
    while d:
        large = None
        if d[-1] > d[0]:
            large = d.pop()
        else:
            large =d.popleft()
        if len(d) == 0:
            return "Yes"
        if d[-1] > large or d[0] > large:
            return "No"
for i in range(int(input())):
    no_of_cubes = int(input())
    d = deque(map(int, input().split()))
    print(piling(d))
