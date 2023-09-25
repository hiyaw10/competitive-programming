class Solution(object):
    def bestTeamScore(self, scores, ages):
        """
        :type scores: List[int]
        :type ages: List[int]
        :rtype: int
        """
        
        pairs = sorted([[scores[i], ages[i]] for i in range(len(scores))])
        dpArray = [pairs[i][0] for i in range(len(pairs))]
        
        for i in range(len(pairs)):
            newScore, mAge = pairs[i]
            for j in range(i):
                score, age = pairs[j]
                if mAge >= age:
                    dpArray[i] = max(newScore + dpArray[j], dpArray[i])
        return max(dpArray)
        
