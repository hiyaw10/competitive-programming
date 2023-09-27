class WordDictionary(object):

    def __init__(self):
        self.d = {}
        
    def addWord(self, word):
        current = self.d
        if not self.search(word):
            for i in range(len(word)):
                if word[i] not in current:
                    current[word[i]] = {}
                current = current[word[i]]
            current["#"] = {}
        
    def search(self, word):
        current = self.d
        def rec(start, current):
            if start >= len(word):
                if "#" in current:
                    return True
                else: return False
            
            if word[start] == ".":
                for k, v in current.items():
                    if rec(start+1, v):
                        return True
                return False
            elif word[start] in current:
                if rec(start+1, current[word[start]]):
                    return True
            else:
                return False
        return rec(0, current)

