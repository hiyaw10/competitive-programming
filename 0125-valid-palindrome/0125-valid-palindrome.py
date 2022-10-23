class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""
        for c in s: #for every character in out input
            if c.isalnum(): #if that character is an alpha numeric character
                newStr += c.lower() #We just push it on to newStr(but lower).
        return newStr == newStr[::-1] #after pushing every single character onto our new string, we return true if its reversed self is the same as itself.
            
        