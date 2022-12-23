class Solution:
    def freqAlphabets(self, s: str) -> str:
        hashmap = {}
        List = []
        
        stack = [i for i in s]
        
        
        words = "abcdefghijklmnopqrstuvwxyz"
        for i in range(len(words)):
            hashmap[str(i+1)] = words[i]
        
        while stack:
            if stack[-1] == "#":
                stack.pop()
                x = stack.pop()
                y = stack.pop()
                List.append(hashmap[y+x])
            else:
                List.append(hashmap[stack.pop()]) 
        List.reverse()
        return "".join(List)
                
            