class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        count1 = 0
        count2 = 0
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] in "aeiouAEIOU":
                count1 += 1
            if s[r] in "aeiouAEIOU":
                count2 += 1
            l += 1
            r -= 1
        return count1 == count2
        