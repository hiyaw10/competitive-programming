class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        countS = Counter(s[:len(p)])
        countP = Counter(p[:len(p)])
        res = []
        if countS == countP:
            res.append(0)
            
        l = 0
        for r in range(len(p), len(s)):
            countS[s[l]] -= 1
            countS[s[r]] = countS.get(s[r], 0) + 1
            
            
            if countS[s[l]] == 0:
                del countS[s[l]]
            l += 1
            
            if countS and countP and countS == countP:
                res.append(l)
        return res
    
