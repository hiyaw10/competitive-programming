class Solution:
    def addDigits(self, num: int) -> int:
        while(len(str(num)) > 1):
            num = sum([int(a) for a in list(str(num))])
        return num
