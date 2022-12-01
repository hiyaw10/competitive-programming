class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned_words = set(banned)
        ans = ""
        max_count = 0
        word_count = defaultdict(int)
        word_buffer = []

        for p, char in enumerate(paragraph):
            
            if char.isalnum():
                word_buffer.append(char.lower())
                if p != len(paragraph)-1:
                    continue

            
            if len(word_buffer) > 0:
                word = "".join(word_buffer)
                if word not in banned_words:
                    word_count[word] +=1
                    if word_count[word] > max_count:
                        max_count = word_count[word]
                        ans = word
                
                word_buffer = []

        return ans
        