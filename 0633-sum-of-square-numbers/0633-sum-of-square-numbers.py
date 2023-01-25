class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l, r = 0, int(c**0.5)
        while r >= l:
            potentialAns = l**2 + r**2
            if potentialAns > c:
                r -= 1
            elif potentialAns < c:
                l += 1
            else:
                return True
        return False
        