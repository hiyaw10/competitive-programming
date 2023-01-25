class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1, p2, holder = m-1, n-1, m+n - 1
        
        while p2 >= 0 and p1 >= 0:
            if nums2[p2] >= nums1[p1]:
                nums1[holder] = nums2[p2]
                holder -= 1
                p2 -= 1
            else:
                nums1[holder] = nums1[p1]
                p1 -= 1
                holder -= 1
        if p2 >= 0:
            for i in range(p2+1):
                nums1[i] , nums2[i] = nums2[i], nums1[i]
        return nums1
                