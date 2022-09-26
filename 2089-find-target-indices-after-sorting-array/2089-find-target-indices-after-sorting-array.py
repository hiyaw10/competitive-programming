class Solution:
    # brute force via sorting and linear search
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        return [idx for idx, num in enumerate(nums) if num == target]
    
    # counter based
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        counts = collections.Counter(nums)
        smallEles = sum(ele for key, ele in counts.items() if key < target)
        
        return list(range(smallEles, smallEles + counts[target]))