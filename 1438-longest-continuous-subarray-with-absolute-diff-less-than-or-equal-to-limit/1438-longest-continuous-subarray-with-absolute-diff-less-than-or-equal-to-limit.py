from collections import deque
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        minQ = deque()
        maxQ = deque()
        
        left, ans = 0, 0
        
        #when do we add to the minQ(trying the list )
        for right in range(len(nums)):
            while minQ and minQ[-1] > nums[right]:
                minQ.pop()
            minQ.append(nums[right])
        #when do we add to the maxQ
            while maxQ and maxQ[-1] < nums[right]:
                maxQ.pop()
            maxQ.append(nums[right])
        #check the subarray
            while limit < abs(maxQ[0] - minQ[0]):
                val = nums[left]
                if maxQ[0] == val:
                    maxQ.popleft()
                if minQ[0] == val:
                    minQ.popleft()
                left += 1
            ans = max(ans, right-left+1)
        return ans