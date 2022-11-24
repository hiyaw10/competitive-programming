class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashmap1 = {}
        hashmap2 = {}
        res = []
        for num in nums1:
            if num in hashmap1:
                hashmap1[num] += 1
            else:
                hashmap1[num] = 1
        for num in nums2:
            if num in hashmap2:
                hashmap2[num] += 1
            else:
                hashmap2[num] = 1
        #we have created a hashmap of their frequency
        for key in hashmap1:
            if key in hashmap2:
                freq = min(hashmap1[key],hashmap2[key])
                for i in range(freq):
                    res.append(key)
            else:
                continue
        return res
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # nums1.sort()
        # nums2.sort()
        # l, r = 0, 0
        # res = []
        # while l < len(nums1) and r < len(nums2):
        #     if nums1[l] == nums2[r]:
        #         res.append(nums1[l])
        #         l += 1
        #         r += 1
        #     elif nums1[l] > nums2[r]:
        #         r += 1
        #     else:
        #         l += 1
        # return res