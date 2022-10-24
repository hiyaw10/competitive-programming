class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        new_str = ""
        new_str2 = ""
        for word in word1:
            new_str += word
        for word in word2:
            new_str2 += word
        return new_str == new_str2
            
        