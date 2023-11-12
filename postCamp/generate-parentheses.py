class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(temp, left, right, stack):
            if left == right == 0:
                res.append(temp)
                return
            
            if left > 0:
                backtrack(temp + "(", left - 1, right, stack + 1)
                
            if right > 0 and stack > 0:
                backtrack(temp + ")", left, right - 1, stack - 1)
                
        backtrack("", n , n, 0)
        
        return res
                