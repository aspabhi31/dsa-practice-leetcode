# 130. Surrounded Regions
# You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded: Connect: A
# cell is connected to adjacent cells horizontally or vertically. Region: To form a region connect every 'O' cell.
# Surround: A region is surrounded if none of the 'O' cells in that region are on the edge of the board. Such regions
# are completely enclosed by 'X' cells. To capture a surrounded region, replace all 'O's with 'X's in -place within the
# original board. You do not need to return anything.

# Example 1:
# Input: board = [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
# Output: [["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "O", "X", "X"]]
# Explanation:
# In the above diagram, the bottom region is not captured because it is on the edge of the board and cannot be surrounded.

# Example 2:
# Input: board = [["X"]]
# Output: [["X"]]

# Constraints:
# m == board.length
# n == board[i].length
# 1 <= m, n <= 200
# board[i][j] is 'X' or 'O'.

# Depth-First Search (DFS) Recursive
def dfs(row, column, board):
    if row<0 or column<0 or row>=len(board) or column>=len(board[0]) or board[row][column]!='O':
        return
    board[row][column]='#'
    dfs(row+1, column, board)
    dfs(row-1, column, board)
    dfs(row, column+1, board)
    dfs(row, column-1, board)

def solve(board):
    if not board:
        return
    rows=len(board)
    cols=len(board[0])
    for row in range(rows):
        if board[row][0]=='O':
            dfs(row, 0, board)
        if board[row][cols-1]=='O':
            dfs(row, cols-1, board)
    for col in range(cols):
        if board[0][col]=='O':
            dfs(0, col, board)
        if board[rows-1][col]=='O':
            dfs(rows-1, col, board)
    for row in range(rows):
        for col in range(cols):
            if board[row][col]=='O':
                board[row][col]='X'
            elif board[row][col]=='#':
                board[row][col]='O'

board = [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
solve(board)
print(board)
