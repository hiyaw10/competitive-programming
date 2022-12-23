class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        #t = s + one more letter
        S = Counter(s)
        T = Counter(t)
        for n in T:
            if n not in S or S[n] != T[n]:
                return n