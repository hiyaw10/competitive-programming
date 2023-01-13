class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        output = 0
        for i in range(len(strs[0])):
            temp = []
            for j in range(len(strs)):
                temp.append(strs[j][i]) 
            
            if sorted(temp) != temp :
                output += 1
        return (output)