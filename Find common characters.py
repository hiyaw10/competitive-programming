class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        length = len(words)
        letters = [[0 for i in range(length)] for i in range(26)]
        
        for i in range(len(words)):
            for j in range(len(words[0])):
                char = ord(words[i][j]) - 97
                letters[char][i] += 1
        
        ans = []
        for i in range(26):
            Min = min(letters[i])
            
            for _ in range(Min):
                ans.append(chr(i + 97))

        return ans
                
        
        
