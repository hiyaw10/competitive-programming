class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        tempr = []
        templ = []
        piv = []
        for num in nums:
            if num < pivot:
                tempr.append(num)
            elif num > pivot:
                templ.append(num)
            else:
                piv.append(num)
        
        return tempr+piv + templ