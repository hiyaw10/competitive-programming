class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        Stack = []
        for c in s:
            Stack.append(c)
        i = 0
        while Stack:
            s[i] = Stack.pop()
            i += 1