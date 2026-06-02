# 200. Number of Islands
# Given an m x n 2D binary grid, grid which represents a map of '1's(land) and '0's(water), return the number of islands.
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.You may assume
# all four edges of the grid are all surrounded by water.

# Example 1:
# Input: grid = [
#     ["1", "1", "1", "1", "0"],
#     ["1", "1", "0", "1", "0"],
#     ["1", "1", "0", "0", "0"],
#     ["0", "0", "0", "0", "0"]
# ]
# Output: 1

# Example 2:
# Input: grid = [
#     ["1", "1", "0", "0", "0"],
#     ["1", "1", "0", "0", "0"],
#     ["0", "0", "1", "0", "0"],
#     ["0", "0", "0", "1", "1"]
# ]
# Output: 3

# Constraints:
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] is '0' or '1'.

# Depth-First Search(DFS)
def dfs(row, column, grid):
    if row<0 or column<0 or row>=len(grid) or column>=len(grid[0]) or grid[row][column]=='0':
        return
    grid[row][column]='0'
    dfs(row+1, column, grid)
    dfs(row-1, column, grid)
    dfs(row, column+1, grid)
    dfs(row, column-1, grid)

def number_of_islands_1(grid):
    if not grid:
        return 0
    rows=len(grid)
    cols=len(grid[0])
    count=0
    for row in range(rows):
        for column in range(cols):
            if grid[row][column]=='1':
                count+=1
                dfs(row, column, grid)
    return count

#Breadth-First Search(BFS)
from collections import deque
def number_of_islands_2(grid):
    if not grid:
        return 0
    rows=len(grid)
    cols=len(grid[0])
    count=0
    directions=[(0,1),(1,0),(-1,0),(0,-1)]
    for row in range(rows):
        for column in range(cols):
            if grid[row][column]=="1":
                count+=1
                grid[row][column]="0"
                q=deque([(row, column)])
                while q:
                    x, y=q.popleft()
                    for dx, dy in directions:
                        nx, ny=x+dx, y+dy
                        if 0<=nx<rows and 0<=ny<cols and grid[nx][ny]=="1":
                            grid[nx][ny]="0"
                            q.append((nx, ny))
    return count

grid = [
     ["1", "1", "0", "0", "0"],
     ["1", "1", "0", "0", "0"],
     ["0", "0", "1", "0", "0"],
     ["0", "0", "0", "1", "1"]
]
print(number_of_islands_1(grid))
grid = [
     ["1", "1", "0", "0", "0"],
     ["1", "1", "0", "0", "0"],
     ["0", "0", "1", "0", "0"],
     ["0", "0", "0", "1", "1"]
]
print(number_of_islands_2(grid))