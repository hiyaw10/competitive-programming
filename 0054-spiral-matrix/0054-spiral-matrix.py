class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        visited = set()
        cols, rows = len(matrix[0]), len(matrix)
        row, col = 0, 0
        d_row, d_col = 0, 1
        result = []

        for _ in range(cols * rows):
            visited.add((row, col))
            result.append(matrix[row][col])

            if not (0 <= (row + d_row) < rows and 0 <= (col + d_col) < cols and (row + d_row, col + d_col) not in visited):
                d_row, d_col = d_col, -d_row

            row += d_row
            col += d_col

        return result
        