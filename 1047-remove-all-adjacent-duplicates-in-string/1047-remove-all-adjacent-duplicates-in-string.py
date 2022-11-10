class Solution:
    def removeDuplicates(self, s: str) -> str:
        """
        We need a stack data structure to solve this question.
        Whenever we find an integer similar we just remove the left most from the stack
        otherwise we just append it onto our stack
        after we scan through the list, we finally return our stack
        """
        stack = []
        for c in s:
            if stack and c == stack[-1]:
                stack.pop(-1)
            else:
                stack.append(c)
        return "".join(stack)