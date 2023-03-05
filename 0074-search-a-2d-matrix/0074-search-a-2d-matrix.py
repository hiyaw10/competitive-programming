class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        j = 0
        for i in range(len(matrix)):
            if target >= matrix[i][0]:
                   j = i
        
        SET = set(matrix[j])
        if target in SET:
            return True
        return False
        
       
        