class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) != 1:
            y = max(stones)
            stones.remove(y)
            x = max(stones)
            stones.remove(x)
            
            if x == y:
                pass
            stones.append(abs(y - x))
        return stones[0]
        