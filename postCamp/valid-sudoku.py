class Solution(object):
    def isValidSudoku(self, board):
        rows = len(board)
        columns = len(board[0]) if rows > 0 else 0
        block = defaultdict(set)
        criterias = 0
        
        for col in range(columns):
            hashSet = set()
            for row in range(rows):
                element = board[row][col]
                if element in hashSet:
                    return False
                elif element != ".":
                    hashSet.add(element)
        criterias += 1

        for row in range(rows):
            hashSet2 = set()
            for col in range(columns):
                element = board[row][col]
                if element in hashSet2:
                    return False
                elif element != ".":
                    hashSet2.add(element)
        criterias += 1
        
        for r in range(rows):
            for c in range(columns):
                if board[r][c] != "." and board[r][c] in block[(r//3, c//3)]:
                    return False
                block[(r//3, c//3)].add(board[r][c])
        criterias += 1
        
        return criterias == 3
        
        
        
        