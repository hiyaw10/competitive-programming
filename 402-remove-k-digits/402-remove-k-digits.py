class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        n = len(num)
        if n == k:
            return '0'
        s=[]
        for i in num:
            while s and s[-1]>i and k>0:
                s.pop()
                k-=1
            s.append(i)
        
        if k>0:
            for i in range(k):
                s.pop()
        
        if s[0]=='0':
            while s and s[0]=='0':
                s.pop(0)
            return "".join(s) if s else '0'
        else:
            return ''.join(s)
        