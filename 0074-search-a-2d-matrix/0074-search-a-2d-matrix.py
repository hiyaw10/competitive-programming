class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        array = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                array.append(matrix[i][j])
        arr1 = set(array)
        if target in arr1:
            return True
        return False
        