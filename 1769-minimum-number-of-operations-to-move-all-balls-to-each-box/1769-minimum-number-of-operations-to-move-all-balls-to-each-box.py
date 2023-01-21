class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ind = []
        ans = []
        
        for i in range(len(boxes)):
            if boxes[i] == "1":
                ind.append(i)
                
        Sum = 0
        for i in range(len(boxes)):
            for j in range(len(boxes)):
                if j != i and boxes[j] == "1":
                    Sum += abs(j - i)
            ans.append(Sum)
            Sum = 0
        return ans