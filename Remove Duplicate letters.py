class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        #remove duplicates and make it lexicographically correct!
        stack = []
        seen = set()
        hashmap = {}
        for i in range(len(s)):
            hashmap[s[i]] = i
        
        
        for i in range(len(s)):
            if s[i] in seen: continue
            while stack and stack[-1] > s[i] and hashmap[stack[-1]] > i:
                seen.remove(stack[-1])
                stack.pop()
            stack.append(s[i])
            seen.add(s[i])
        return "".join(stack)
