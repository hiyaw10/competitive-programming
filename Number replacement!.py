testCases = int(input())
for i in range(testCases):
    length = int(input())
    num = list(map(int, input().split()))
    char = input()
    
    
    hashmap = {}
    x = 1
    for i in range(len(num)):
        if num[i] in hashmap:
            if hashmap[num[i]] != char[i]:
                x = 0
            else:
                continue
        else:
            hashmap[num[i]] = char[i]
        
    if x == 1:
        print("YES")
    else:
        print("NO")
