from math import log2
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return log2(n).is_integer() if n > 0 else False