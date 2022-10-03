class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # using stack make a ngr 
        stack = []
        ngr = []
        for i in reversed(range(len(nums2))):
            while stack and nums2[i]>= stack[-1]:
                stack.pop()
            if not stack:
                ngr.append(-1)
            else:
                ngr.append(stack[-1])
            stack.append(nums2[i])
        ngr = ngr[::-1]
        val_to_id = {}
        for i,val in enumerate(nums2):
            val_to_id[val] = i
        ans = []
        for val in nums1:
            ans.append(ngr[val_to_id[val]])
        return ans
        