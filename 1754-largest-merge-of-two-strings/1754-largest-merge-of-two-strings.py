class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        ans = []
        
        p1, p2 = 0, 0
        while p1 < len(word1) and p2 < len(word2):
            if word1[p1] == word2[p2]:
                if word1[p1:] >= word2[p2:]:
                    ans.append(word1[p1])
                    p1 += 1
                else:
                    ans.append(word2[p2])
                    p2 += 1
            elif word1[p1] > word2[p2]:
                ans.append(word1[p1])
                p1 += 1
            else:
                ans.append(word2[p2])
                p2 += 1
        ans.extend(word1[p1:])
        ans.extend(word2[p2:])
        return "".join(ans)