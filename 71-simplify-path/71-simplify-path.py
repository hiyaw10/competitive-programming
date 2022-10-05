class Solution:
    def simplifyPath(self, path: str) -> str:
        l=path.split("/")
        stack=[]
        ans="/"
        for i in l:
            if i=="." or i=="":
                continue
            elif len(stack)!=0 and i=="..":
                stack.pop()
            elif len(stack)==0 and i=="..":
                continue
            else:
                stack.append(i)
        ans=ans+"/".join(stack)
        return ans