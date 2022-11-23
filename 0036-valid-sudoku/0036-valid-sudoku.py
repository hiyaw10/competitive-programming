
class Solution:
    def isValidSudoku(self, board):
        for row in chain(board, zip(*board)):
            cand = [i for i in row if i != "."]
            if len(set(cand)) != len(cand): return False
            
        for x, y in product([1,4,7],[1,4,7]):
            cand = [board[x+i][y+j] for i,j in product([-1,0,1],[-1,0,1])]
            cand = [i for i in cand if i != "."]
            if len(set(cand)) != len(cand): return False

        return True
        
          