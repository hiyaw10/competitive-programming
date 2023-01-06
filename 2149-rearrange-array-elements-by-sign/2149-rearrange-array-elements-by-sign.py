class Solution(object):
    def rearrangeArray(self, nums):
        pos = []
        neg = []
        output = [0] * len(nums)
        for i in nums:
            if i > 0:
                pos.append(i)
            if i < 0:
                neg.append(i)
        j = 0
        for i in pos:
            output[j] = i
            j += 2
        j = 1
        for i in neg:
            output[j] = i
            j += 2
        return output