class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        intial = [-1]
        
        for i in range(len(arr) - 1, 0, -1):
            intial.append(max(intial[-1], arr[i]))
        intial.reverse()
        return intial