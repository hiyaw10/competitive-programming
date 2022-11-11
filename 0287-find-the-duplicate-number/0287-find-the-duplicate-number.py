class Solution(object):
    def findDuplicate(self, nums):
        has = set()
        for c in nums:
            if c in has:
                return c
            else:
                has.add(c)