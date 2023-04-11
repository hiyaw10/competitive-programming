class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:        
        def get_gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a
        
        return reduce(get_gcd, Counter(deck).values()) > 1