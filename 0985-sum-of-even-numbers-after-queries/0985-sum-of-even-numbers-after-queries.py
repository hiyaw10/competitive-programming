class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        temp = []
        even = 0
        for i in nums:
            if i % 2 == 0:
                even += i
        
        for num, index in queries:
            if nums[index] % 2 == 0:
                even -= nums[index]
            nums[index] += num
            if nums[index] % 2 == 0:
                even += nums[index]
            temp.append(even)
        return temp
            
                    