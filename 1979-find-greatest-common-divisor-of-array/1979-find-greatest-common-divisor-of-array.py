class Solution:
    def findGCD(self, nums: List[int]) -> int:
        potentialGCD = min(nums)
        Max = max(nums)
        
        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a%b)
        return gcd(Max, potentialGCD)