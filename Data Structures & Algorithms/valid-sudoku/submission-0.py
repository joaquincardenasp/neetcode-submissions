class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        dic = defaultdict(set)
        for i in range(len(board)):
            seen = set()
            for j in range(0,9):
                if board[i][j] not in seen and board[i][j] != '.':
                    seen.add(board[i][j])
                elif board[i][j] == '.':
                    continue
                else:
                    return False
        for j in range(0,9):
            seen_col = set()
            for i in range(0,9):
                if board[i][j] not in seen_col and board[i][j] != '.':
                    seen_col.add(board[i][j])
                elif board[i][j] == '.':
                    continue
                else:
                    return False
        for i in range(0,9):
            for j in range(0,9):
                if board[i][j] != '.' and board[i][j] not in dic[i//3, j//3]:
                    dic[i//3, j//3].add(board[i][j])
                elif board[i][j] == '.':
                    continue
                else:
                    return False
        return True

            