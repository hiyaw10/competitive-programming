class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.Helper(s) == self.Helper(t)    
    def Helper(self, string):
        stack = []
        for char in string:
            if stack and char == "#":
                stack.pop()
            elif char != "#":
                stack.append(char)
        return "".join(stack)
    
    
    