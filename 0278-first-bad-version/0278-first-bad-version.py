# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low, high = 1, n
        ans = 0
        
        while low <= high:
            mid = low  + (high - low) // 2
            
            if isBadVersion(mid) == False:
                low = mid + 1
            else:
                high = mid - 1
                ans = mid
        return ans