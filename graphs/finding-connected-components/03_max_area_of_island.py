# 695. Max Area of Island
# You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally
# (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water. The area of an island is
# the number of cells with a value 1 in the island. Return the maximum area of an island in grid.If there is no island,
# return 0.

# Example 1:
# Input: grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
#                [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
#                [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
#                [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
# Output: 6
# Explanation: The answer is not 11, because the island must be connected 4 - directionally.

# Example 2:
# Input: grid = [[0, 0, 0, 0, 0, 0, 0, 0]]
# Output: 0

# Constraints:
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 50
# grid[i][j] is either 0 or 1.

# Depth-First Search (DFS) Iterative
def max_area_of_island_1(grid):
    rows=len(grid)
    cols=len(grid[0])
    max_area=0
    for row in range(rows):
        for col in range(cols):
            if grid[row][col]==1:
                area=0
                grid[row][col]=0
                directions=[(0, 1), (1, 0), (0, -1), (-1, 0)]
                stack=[(row, col)]
                while stack:
                    x, y=stack.pop()
                    area+=1
                    for dx, dy in directions:
                        nx, ny=x+dx, y+dy
                        if 0<=nx<rows and 0<=ny<cols and grid[nx][ny]==1:
                            grid[nx][ny]=0
                            stack.append((nx, ny))
                max_area=max(area, max_area)
    return max_area

# Breadth-First Search (BFS)
from collections import deque
def max_area_of_island_2(grid):
    rows=len(grid)
    cols=len(grid[0])
    max_area=0
    for row in range(rows):
        for col in range(cols):
            if grid[row][col]==1:
                area=0
                grid[row][col]=0
                directions=[(0, 1), (1, 0), (0, -1), (-1, 0)]
                q=deque([(row, col)])
                while q:
                    x, y=q.popleft()
                    area+=1
                    for dx, dy in directions:
                        nx, ny=x+dx, y+dy
                        if 0<=nx<rows and 0<=ny<cols and grid[nx][ny]==1:
                            grid[nx][ny]=0
                            q.append((nx, ny))
                max_area=max(area, max_area)
    return max_area

#Depth-First Search (DFS) Recursive
def dfs(row, col, grid):
    if row<0 or row>=len(grid) or col<0 or col>=len(grid[0]) or grid[row][col]==0:
        return 0
    grid[row][col]=0
    return (1+dfs(row+1, col, grid)+dfs(row-1, col, grid)+dfs(row, col+1, grid)+dfs(row, col-1, grid))

def max_area_of_island_3(grid):
    rows=len(grid)
    cols=len(grid[0])
    max_area=0
    for row in range(rows):
        for col in range(cols):
            if grid[row][col]==1:
                max_area=max(max_area, dfs(row, col, grid))
    return max_area


grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
               [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
               [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
print(max_area_of_island_1(grid))
grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
               [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
               [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
print(max_area_of_island_2(grid))
grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
               [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
               [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
print(max_area_of_island_3(grid))