class Solution:
    def threeSumMulti(self, A, t):
        ans = 0
        n = len(A)
        level2 = collections.defaultdict(int)
        for i in range(2, n):
            for j in range(i-1):
                level2[A[j] + A[i-1]] += 1
            ans = ans + level2[t - A[i]]
            ans = ans % (10**9 + 7)
        return ans