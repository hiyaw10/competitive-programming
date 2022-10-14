class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        #prefix array
        sums = [0] * (len(gain) + 1) #List Generation
        for i in range(len(gain)):
            sums[i+1] = sums[i] + gain[i] #curr number plus 
        return max(sums)
        