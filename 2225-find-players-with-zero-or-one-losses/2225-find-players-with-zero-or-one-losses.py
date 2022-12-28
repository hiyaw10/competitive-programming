class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        hashmap = {}
        output = [[],[]]
        for win, lose in matches:
            hashmap[win] = 0
            hashmap[lose] = 0
        for i in matches:
            hashmap[i[1]] -= 1
        for team, loss in hashmap.items():
            if loss == 0:
                output[0].append(team)
            if loss == -1:
                output[1].append(team)
        output[0].sort()
        output[1].sort()
        return output
            
                
                