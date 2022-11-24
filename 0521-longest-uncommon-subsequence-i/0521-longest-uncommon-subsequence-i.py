class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        # l, r = 0, 0
        # maxR = 0
        # while r < len(a):
        #     if a[r] not in b:
        #         r += 1
        #         diff = r - l
        #         maxR= max(diff, maxR)
        #     else:
        #         l = r + 1
        #         r += 2
        # return maxR

        if a == b:
            return -1
        return max(len(a), len(b))