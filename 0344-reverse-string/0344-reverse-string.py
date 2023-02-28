class Solution(object):
    def reverseString(self, s):
        def reverse(l, r):
            if l < r:
                s[l], s[r] = s[r], s[l]
                reverse(l+1, r-1)
        return reverse(0, len(s)-1)