class Solution(object):
    def lastStoneWeightII(self, stones):
        weight = sum(stones)
        
        target = int(weight / 2)
        array = [0] * (int(target)+1)

       
        for stone in stones:
            for j in range(target, stone-1, -1):
                array[j] = max(array[j], array[j-stone]+stone)

        return weight - 2 * array[-1]
