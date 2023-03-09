class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        Str = s + s
        
        new = ""
        
        for i,n in enumerate(Str):
            if i == 0:
                continue
            if i == len(Str) - 1:
                continue
            else:
                new += n
        
        

        
        if s in new:
            return True
        return False
       