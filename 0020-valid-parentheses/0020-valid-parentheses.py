class Solution:
    def isValid(self, s: str) -> bool:
        #open brackets must be closed
        #in the correct order(stack problem)
        stack = []
        Map = {")":"(", "}":"{", "]":"["}
        for c in s:
            if c in Map: #closing parenthesis
                if stack and stack[-1] == Map[c]:
                    stack.pop() #continue going
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False