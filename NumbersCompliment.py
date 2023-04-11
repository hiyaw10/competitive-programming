class Solution:
    def findComplement(self, num: int) -> int:
        new = str(bin(num)[2:])        
        
        ans = []
        for c in new:
            if c == "1":
                ans.append("0")
            else:
                ans.append("1")
        final = "".join(ans)
        
        return int(final, 2)
