class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        best = 0
        front = -1
        for i, c in enumerate(s):
            
            if c in seen and front < seen[c]:
                front = seen[c]
                
            seen[c] = i
            
            if (i - front) > best:
                best = i - front
            
        return best