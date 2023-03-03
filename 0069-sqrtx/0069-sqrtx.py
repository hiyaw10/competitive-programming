class Solution:
    
    def mySqrt(self, x: int) -> int:
        low, high = 0, x//2
        if x <= 1:
            return x
        while low <= high:
            mid = int(low + (high-low)/2)
            if mid > int(x ** 0.5):
                high = mid - 1
            elif mid < int(x ** 0.5):
                low = mid + 1
            else:
                return mid
            
            
            