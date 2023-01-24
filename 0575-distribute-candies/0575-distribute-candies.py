class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        Type = len(set(candyType))
        Edible = len(candyType) // 2
        return min(Type, Edible)
            