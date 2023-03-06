class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l, r = -1, len(arr)
        
        while l + 1  < r:
            mid = l + (r-l)//2
            if arr[mid] < arr[mid-1]:
                r = mid
            else:
                l = mid
        if l == -1:
            return 1
        
        return l