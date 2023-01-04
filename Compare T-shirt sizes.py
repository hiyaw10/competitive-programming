testCases = int(input())
for i in range(testCases):
    a,b = input().split()
   
    L1, L2 = len(a), len(b)
    x = 0
    if a[-1] == b[-1]:
        if len(a) == len(b):
            x = 0
        elif len(a) < len(b):
            if a[-1] == "S":
                x = 1
            else:
                x = 2
        else:
            if a[-1] == "S":
                x = 2
            else:
                x = 1
    elif a[-1] == "S" and b[-1] == "L":
        x = 2
    elif a[-1] == "L" and b[-1] == "S":
        x = 1
    elif a[-1] == "M" and b[-1] == "S":
        x = 1
    elif a[-1] == "M" and b[-1] == "L":
        x = 2
    elif a[-1] == "S" and b[-1] == "M":
        x = 2
    else:
        x = 1
    if x == 0:
        print("=")
    elif x == 1:
        print(">")
    else:
        print("<")
