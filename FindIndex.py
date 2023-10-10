class Solution(object):
    def strStr(self, haystack, needle):
        
        for r in range(len(haystack)):
            
            p1, p2 = r, 0
            start = r
            while p1 < len(haystack) and p2 < len(needle) and haystack[p1] == needle[p2]:
                p2 += 1
                p1 += 1
                
                if len(needle) == p2:
                    return start
        return -1
                
