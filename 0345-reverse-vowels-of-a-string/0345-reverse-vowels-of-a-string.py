class Solution:
    def reverseVowels(self, s: str) -> str:
        lst = list(s)
        l, r = 0, len(s) - 1
        while l < r:
            if lst[r] not in "aeiouAEIOU":
                r -= 1
            elif lst[l] not in "aeiouAEIOU":
                l += 1
            else:
                lst[r], lst[l] = lst[l], lst[r]
                l += 1
                r -= 1
        return "".join(lst)