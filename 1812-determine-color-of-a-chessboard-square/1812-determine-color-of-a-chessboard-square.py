class Solution:
    def squareIsWhite(self, c: str) -> bool:
        e,o = ["b","d","f","h"], ["a","c","e","g"]
        if int(c[-1]) % 2 == 0:
            if c[0] in e: return False
            else: return True
        else:
            if c[0] in e: return True
            else: return False
