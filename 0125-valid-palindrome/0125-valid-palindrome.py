class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ""
        for char in s:
            if char.isalnum():
                res += char.lower()
        if res == res[::-1]:
            return True
        return False