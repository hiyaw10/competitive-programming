class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for i in range(len(logs)):
            if logs[i] == "../":
                if stack: stack.pop(-1)
            elif logs[i] == "./":
                continue
            else:
                stack.append(logs[i])
        return len(stack)