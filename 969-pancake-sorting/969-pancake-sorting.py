class Solution:
	def pancakeSort(self, arr: List[int]) -> List[int]:
		n = len(arr)
		ans = []
		sorted_array = [i + 1 for i in range(n)]
		max_val = n

		while arr != sorted_array and max_val > 0:
			index = 0

			if arr[0] == max_val:
				ans.append(max_val)
				arr[:max_val] = arr[:max_val][::-1]
				max_val -= 1

			else:                
				for i in range(n):
					if arr[i] == max_val:
						index = i

				arr[:index+1] = arr[:index+1][::-1]
				ans.append(index + 1)

		return ans