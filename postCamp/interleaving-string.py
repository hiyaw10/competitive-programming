class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        @lru_cache
        def is_inter(p1: int, p2: int) -> bool:
            p3 = p1+p2
            if p1>n1 and p2>n2:
                return p3>n3
            if p1>n1 and p3>n3:
                return p2>n2
            if p2>n2 and p3>n3:
                return p1>n1
            if p3>n3:
                return False
            if p1<=n1 and s1[p1]==s3[p3] and is_inter(p1+1, p2):
                return True
            if p2<=n2 and s2[p2]==s3[p3] and is_inter(p1, p2+1): 
                return True
            return False
                
        n1, n2, n3 = len(s1)-1, len(s2)-1, len(s3)-1
        return is_inter(0, 0)