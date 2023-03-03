class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights) - 1
        right = sum(weights) + 1
        
        while left + 1 < right:
            mid = (left + right)//2
            
            var = 1
            temp = 0
            for i in weights:
                temp += i
                if temp > mid:
                    var += 1
                    temp = i
            
                            
            if var > days:
                left = mid
            else:
                right = mid
        return right 