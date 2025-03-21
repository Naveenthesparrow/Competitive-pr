Question Name: N-Queens


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n == 1:
            return ['Q']
        if n == 2 or n == 3:
            return []
        solutions = []
        board = [['.'] * n for _ in range(n)]
        self.positions(n, board, 0, solutions)
        return solutions

    def positions(self, n, board, col, solutions):
        if n <= col:
            solutions.append([''.join(row) for row in board])
            return
        for i in range(n):
            if self.is_position_safe(n, board, i, col):
                board[i][col] = 'Q'
                self.positions(n, board, col + 1, solutions)
                board[i][col] = '.'
    
    def is_position_safe(self, n, board, row, col):
        for i in range(n):
            if board[row][i] == 'Q' or board[i][col] == 'Q':
                return False
        for i in range(1, n):
            if row - i >= 0 and col - i >= 0 and board[row-i][col-i] == 'Q':
                return False
            elif row + i < n and col + i < n and board[row+i][col+i] == 'Q':
                return False
            elif row - i >= 0 and col + i < n and board[row-i][col+i] == 'Q':
                return False
            elif row + i < n and col - i >= 0 and board[row+i][col-i] == 'Q':
                return False
        return True