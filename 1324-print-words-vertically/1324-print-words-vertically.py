class Solution:
    def printVertically(self, s: str) -> List[str]:
        s = list(s.split())
        output = []
        L = len(max(s, key = len))
        for i in range(L):
            Temp = []
            for j in range(len(s)):
                try:
                    Temp.append(s[j][i])
                except:
                    Temp.append(" ")
            
            output.append("".join(Temp))
        for i in range(len(output)):
            output[i] = output[i].rstrip()
            
        return output
                
        