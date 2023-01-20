class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashmap1 = Counter(nums1)
        hashmap2 = Counter(nums2)
        array = []
        for i in hashmap1:
            if i in hashmap2:
                freq = min(hashmap2[i], hashmap1[i])
                for _ in range(freq):
                    array.append(i)
        return array