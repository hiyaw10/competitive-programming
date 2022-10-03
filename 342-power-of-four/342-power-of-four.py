class Solution:
	def isPowerOfFour(self, n: int) -> bool:
		if n==1:
			return True

		if n ==0 or n % 4 !=0:
			return False

		while n % 4 ==0:
			n = n/4
			if n == 1:
				return True

def main():
	sol = Solution()
	sol.isPowerOfFour(n)

if __name__ == '__main__':
	n = 1
	main()