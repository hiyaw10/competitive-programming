class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        dic_list1 = [set() for _ in range(9)]
        dic_list2 = [set() for _ in range(9)]
        dic_list3 = [[set() for _ in range(3)] for _ in range(3)]
        for i in range(9):
            for j in range(9):
                if not board[i][j].isnumeric():
                    continue
                y = i // 3
                x = j // 3
                num = board[i][j]
                if (num in dic_list1[i]) or (num in dic_list2[j]) or (num in dic_list3[x][y]):
                    return False
                else:
                    dic_list1[i].add(num)
                    dic_list2[j].add(num)
                    dic_list3[x][y].add(num)
        return True