class Solution:
    @cache
    def isMatch(self, s: str, p: str) -> bool:

        if not p:
            return not s
        if len(p) > 1:
            if p[1] == '*':
                if not s:
                    return self.isMatch(s, p[2:])
                return self.isMatch(s, p[2:]) or (s[0] == p[0] or p[0] == '.') and self.isMatch(s[1:], p)
            return s and (s[0] == p[0] or p[0] == '.') and self.isMatch(s[1:], p[1:])
        else:
            return len(s) == 1 and (s[0] == p[0] or p[0] == '.')