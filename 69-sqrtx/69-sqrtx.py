class Solution:
    def mySqrt(self, x: int) -> int:
        for i in range(0,x+1):
            if i*i>x:
                return i-1
                break
            elif i*i==x:
                return i
                break