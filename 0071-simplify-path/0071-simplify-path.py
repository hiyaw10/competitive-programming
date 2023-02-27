class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        ans = "/"
        stack = []
        for i in path:
            if stack and i == "..":
                stack.pop()
            elif i != "" and i != ".." and i != ".":
                stack.append(i)
        return ans + "/".join(stack)