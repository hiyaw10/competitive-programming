class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        l, ans, d = 0, 0, defaultdict(int)
        
        for r in range(len(fruits)):
            d[fruits[r]]+= 1

            while len(d) > 2:
                d[fruits[l]]-= 1
                if not d[fruits[l]]: del d[fruits[l]]
                l += 1

            ans = max(ans, r-l+1)
        
        return ans
        