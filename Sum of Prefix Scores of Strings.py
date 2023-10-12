class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.score = 0

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        self.root = TrieNode()
        self.off = ord('a')

        
        for word in words:
            curr = self.root
            for char in word:
                if curr.children[ord(char) - self.off] is None:
                    curr.children[ord(char) - self.off] = TrieNode()
                
                curr = curr.children[ord(char) - self.off]
                curr.score += 1
        
        answer = []
        for word in words:
            score = 0
            curr = self.root
            for char in word:
                curr = curr.children[ord(char) - self.off]
                score += curr.score
            
            answer.append(score)
        
        return answer
