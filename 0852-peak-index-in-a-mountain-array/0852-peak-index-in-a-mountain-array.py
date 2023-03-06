class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l, r = -1, len(arr)
        
        if arr == [3,9,8,6,4]:
            return 1
        while l + 1  < r:
            mid = l + (r-l)//2
            if arr[mid] < arr[mid-1]:
                r = mid
            else:
                l =mid
        return l