class Solution:
    def interpret(self, command: str) -> str:
        stack = [i for i in command]
        res = ""
        while stack:
            if stack[-1] == ")" and stack[-2] == "(":
                stack.pop()
                stack.pop()
                res = "o" + res
            
            elif stack[-1] == ")" and stack[-2] != "(":
                stack.pop()
                stack.pop()
                stack.pop()
                stack.pop()
                res = "al" + res
            else:
                res = stack.pop() + res
        return res