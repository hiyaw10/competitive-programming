class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        output = []
        k = len(nums) + 1
        numset = set(nums)
        for i in range(1, k):
            if i in numset:
                continue
            else:
                output.append(i)
        return output
                
        