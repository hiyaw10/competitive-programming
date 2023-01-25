class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        newSkill = sorted(skill)
        
        l, r = 0, len(skill) - 1
        ans = 0
        ref = newSkill[0] + newSkill[-1]
        while r > l:
            if newSkill[r] + newSkill[l] == ref:
                ans += (newSkill[r] * newSkill[l])
                l += 1
                r -= 1
            else:
                return -1
        return ans