class Solution:
    def frequencySort(self, s: str) -> str:
        res = []
        c = Counter(s)
        List = sorted(c, key = lambda x:c[x], reverse = True)
        for char in List:
            res.append(char*c[char])
        return "".join(res)