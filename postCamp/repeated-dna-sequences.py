class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        
        res = set()
        seen = set()
        
        iterator = len(s) - 10 + 1
        
        for i in range(iterator):
            if s[i:i+10] in seen:
                res.add(s[i:i+10])
            seen.add(s[i:i+10])
        return res
        