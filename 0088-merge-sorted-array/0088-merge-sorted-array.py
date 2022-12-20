class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        k = m + n - 1
        t, b = m-1, n-1
        while t >= 0 and b >= 0:
            if nums1[t] >= nums2[b]:
                nums1[k] = nums1[t]
                k -= 1
                t -= 1
            else:
                nums1[k] = nums2[b]
                k -= 1
                b -= 1
        if b >= 0:
            for i in range(b+1):
                nums1[i] , nums2[i] = nums2[i], nums1[i]
        return nums1
