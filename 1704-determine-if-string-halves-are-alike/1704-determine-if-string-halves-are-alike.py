class Solution(object):
    def halvesAreAlike(self, s):
        counter1 = 0
        counter2 = 0
        l, r = 0, len(s) / 2
        while l < r and r < len(s):
            if s[l] in "aeiouAEIOU":
                counter1 += 1
            if s[r] in "aeiouAEIOU":
                counter2 += 1
            r += 1
            l += 1
        return counter1 == counter2
            