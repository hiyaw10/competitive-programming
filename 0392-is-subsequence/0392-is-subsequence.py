class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
#         res = ""
#         for char in t:
#             if char in s:
#                 res += char
#         return s == res
        if len(s) == 0:
            return True
        if len(t) == 0:
            return False 
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return True if i == len(s) else False