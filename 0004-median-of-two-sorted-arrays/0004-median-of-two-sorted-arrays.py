class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        k = len(nums1) + len(nums2)
        res = []
        for num in nums1:
            res.append(num)
        for num in nums2:
            res.append(num)
        res.sort()
        if k % 2 == 0:
            return (res[k//2] + res[(k//2)-1])/2           
        else:
            return res[k//2]
            
        