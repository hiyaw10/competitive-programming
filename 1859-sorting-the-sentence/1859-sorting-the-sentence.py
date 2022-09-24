class Solution:
    #we have to split the the sentence as a whole!
    def sortSentence(self, s: str) -> str:
        dic = {}
        for i in s.split():
            dic[i[-1]] = i[:-1]

        final = []
        for num, word in sorted(dic.items()):
            final.append(word)
        return " ".join(final)

