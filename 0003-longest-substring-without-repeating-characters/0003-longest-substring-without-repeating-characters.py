class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        
        ans = 0
        left = 0
        for right in range(len(s)):
            
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            ans = max(right - left + 1, ans)
        return ans