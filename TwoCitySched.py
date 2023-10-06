class Solution(object):
    def twoCitySchedCost(self, costs):
        diff = [(i, costs[i][1] - costs[i][0]) for i in range(len(costs))]
        diff = sorted(diff, key = lambda x:x[1])
        res = 0
        n = len(costs)
        for ind, d in diff[:n//2]:
            res += costs[ind][1]
        for ind, d in diff[n//2:]:
            res += costs[ind][0]
        return res
        
    
