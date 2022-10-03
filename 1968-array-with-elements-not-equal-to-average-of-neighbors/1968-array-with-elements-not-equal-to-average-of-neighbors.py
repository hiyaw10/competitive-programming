class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        def swap(l, r):
            nums[l], nums[r] = nums[r], nums[l]
            
        n = len(nums)
        for i in range(1, n-1):
            prev, cur, nxt = nums[i-1], nums[i], nums[i+1]

            if prev < cur < nxt or prev > cur > nxt:
                swap(i+1, i)
                
        return nums
        