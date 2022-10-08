import collections
class Solution:
	def shortestSubarray(self, nums, target):
		d = collections.deque()
		d.append([0,0])
		res = float('inf')
		cur  = 0
		for j in range(len(nums)):
			cur +=nums[j]
			while(d and cur-d[0][1]>=target):
				i = d.popleft()[0]
				res = min(res, j-i+1)
			while(d and cur<=d[-1][1]):
				d.pop()
			d.append([j+1, cur])
		return res if res < float('inf') else -1