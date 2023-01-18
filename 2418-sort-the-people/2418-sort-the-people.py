class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        Map = {}
        for i in range(len(names)):
            Map[heights[i]] = names[i]
        output = []
        for i in range(len(heights) - 1):
            for j in range(len(heights) - 1):
                if heights[j] < heights[j+1]:
                    heights[j], heights[j+1] = heights[j+1], heights[j]
        for i in heights:
            output.append(Map[i])
        return output