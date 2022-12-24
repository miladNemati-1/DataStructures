"""
Valid Sudoku

Solution
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.


Example 1:


Input: board =
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
Example 2:

Input: board =
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.


"""

import time


class Solution:

    def checkColumnsAndRows(self, board):

        for i in range(len(board)):
            row_set = set()
            column_set = set()
            for x in range(len(board)):
                if row_set.__contains__(board[i][x]):
                    return False
                if column_set.__contains__(board[x][i]):
                    return False
                if board[x][i] != '.':
                    column_set.add(board[x][i])
                if board[i][x] != '.':
                    row_set.add(board[i][x])
        return True

    def checkSubBoards(self, board):
        for i in range(3):
            for j in range(3):
                number_set = set()
                for x in range(i*3, i*3+3):
                    for k in range(j*3, j*3+3):
                        if number_set.__contains__(board[x][k]):
                            return False
                        elif board[x][k] != '.':
                            number_set.add(board[x][k])

        return True

    def isValidSudoku(self, board):
        return self.checkColumnsAndRows(board) and self.checkSubBoards(board)


start_time = time.time()

a = Solution().isValidSudoku([[".", ".", ".", ".", "5", ".", ".", "1", "."], [".", "4", ".", "3", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", "3", ".", ".", "1"], ["8", ".", ".", ".", ".", ".", ".", "2", "."], [
    ".", ".", "2", ".", "7", ".", ".", ".", "."], [".", "1", "5", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", "2", ".", ".", "."], [".", "2", ".", "9", ".", ".", ".", ".", "."], [".", ".", "4", ".", ".", ".", ".", ".", "."]])
run_time = time.time() - start_time
print(run_time+1)
print(a)
