class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def backtrack(row):
            if row == n:
                result.append(["".join(r) for r in board])
                return

            for col in range(n):
                # Constraint: column not taken, no diagonal conflicts
                if col in cols or (row - col) in diag1 or (row + col) in diag2:
                    continue

                # CHOOSE: place queen at (row, col)
                board[row][col] = 'Q'
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)

                backtrack(row + 1)

                # UNDO: remove queen from (row, col)
                board[row][col] = '.'
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)
                # EXPLORE: loop tries next col

        board = [['.' for _ in range(n)] for _ in range(n)]
        cols = set()
        diag1 = set()  # row - col constant for "\" diagonal
        diag2 = set()  # row + col constant for "/" diagonal
        result = []

        backtrack(0)
        return result
