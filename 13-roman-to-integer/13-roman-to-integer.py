class Solution:
	def romanToInt(self, s: str) -> int:
		symbols = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
		integer = 0

		i = 0
		while i < len(s):
			if i < len(s)-1 and symbols[s[i]] < symbols[s[i+1]]:
				integer += symbols[s[i+1]]-symbols[s[i]]
				i += 1
			else:
				integer += symbols[s[i]]

			i += 1

		return integer