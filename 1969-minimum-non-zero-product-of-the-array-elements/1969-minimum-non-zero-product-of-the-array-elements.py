class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        return (pow(2**p-2, (2**p-2)//2, 1000000007)*(2**p-1))%1000000007