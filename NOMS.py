class Solution(object):
    def numMatchingSubseq(self, s, words):
        def ans (s,word):
            start =- 1
            for i in word:
                start = s.find(i, start+1)
                if start == -1 :
                    return False
            return True
        res = 0
        for i in words:
            if ans(s, i):
                res += 1
        return res
