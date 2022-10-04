
class Solution:
    def fib(self, n: int) -> int:
        if n==0:
            return(0)
        if n==1:
            return(1)
        else:
            tot = 0
            f0 = 0
            f1 = 1
            while n > 1:
                tot = f0 + f1
                f0 = f1 
                f1 = tot
                n-=1

            return(tot)