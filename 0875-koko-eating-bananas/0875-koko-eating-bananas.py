class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 0, max(piles) + 1
        
        while low < high - 1:
            var = low + (high - low)//2
            
            variable = 0
            
            for i in range(len(piles)):
                variable += ceil(piles[i]/var)
                
            if variable > h:
                low = var
            else:
                high = var
        return high
                
                
            