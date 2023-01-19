class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = Counter(s)
        new = ""
        for i, n in counter.items():
            if n == 1:
                new += i
                break
        for i in range(len(s)):
            if s[i] == new:
                return i
        return -1