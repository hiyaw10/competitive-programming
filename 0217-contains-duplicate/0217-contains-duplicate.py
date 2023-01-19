class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        charset = set()
        for i in nums:
            if i in charset:
                return True
            else:
                charset.add(i)
        