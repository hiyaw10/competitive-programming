class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        res= ""
        output = []
        for n in num:
            res += str(n)
        x = str(int(res) + k)
        for char in x:
            output.append(char)
        return output
        