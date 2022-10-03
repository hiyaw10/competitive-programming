class Solution:
    def calculate(self, s: str) -> int:
        n = len(s)
        num = 0
        stack = []
        sign = '+'
        for i in range(n):
            cur = s[i]
            if cur.isdigit():
                num = num*10 + int(cur)
            if (not cur.isdigit()) and cur != ' ' or i == n - 1:
                if sign == '+':
                    stack.append(num)
                if sign == '-':
                    stack.append((-1)*num)
                if sign == '*':
                    stack[-1] = stack[-1]*num
                if sign == '/':
                    
                    stack[-1] = int(stack[-1] / num)   
                num = 0
                sign = cur
        return sum(stack)