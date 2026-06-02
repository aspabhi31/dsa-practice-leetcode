# 64. Minimum Path Sum
# Given a m x n grid filled with non - negative numbers, find a path from top left to bottom right, which minimizes the
# sum of all numbers along its path. Note: You can only move either down or right at any point in time.

# Example 1:
# Input: grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
# Output: 7
# Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.

# Example 2:
# Input: grid = [[1, 2, 3], [4, 5, 6]]
# Output: 12

# Constraints:
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 200
# 0 <= grid[i][j] <= 200

#Brute Force Recursion
def helper_1(row_index, col_index, grid):
    if row_index == len(grid) or col_index == len(grid[0]):
        return float('inf')
    if row_index==len(grid)-1 and col_index==len(grid[0])-1:
        return grid[row_index][col_index]
    return grid[row_index][col_index]+min(helper_1(row_index+1, col_index, grid), helper_1(row_index, col_index+1, grid))
def min_path_sum_1(grid):
    return helper_1(0, 0, grid)

#Memoization
memo={}
def helper_2(row_index, col_index, grid):
    if row_index == len(grid) or col_index == len(grid[0]):
        return float('inf')
    if row_index==len(grid)-1 and col_index==len(grid[0])-1:
        return grid[row_index][col_index]
    if (row_index, col_index) in memo:
        return memo[(row_index, col_index)]
    memo[(row_index, col_index)]=grid[row_index][col_index]+min(helper_2(row_index+1, col_index, grid), helper_2(row_index, col_index+1, grid))
    return memo[(row_index, col_index)]
def min_path_sum_2(grid):
    return helper_2(0, 0, grid)

#Tabulation
def min_path_sum_3(grid):
    dp=[row[:] for row in grid]
    rows=len(dp)
    cols=len(dp[0])
    for i in range(rows):
        for j in range(cols):
            if i==0 and j==0:
                continue
            top=dp[i-1][j] if i>0 else float('inf')
            left=dp[i][j-1] if j>0 else float('inf')
            dp[i][j]=grid[i][j]+min(top, left)
    return dp[-1][-1]

#Space-Optimized Tabulation
def min_path_sum_4(grid):
    rows = len(grid)
    cols = len(grid[0])
    dp=[float('inf')]*cols
    for i in range(rows):
        for j in range(cols):
            if i==0 and j==0:
                dp[j]=grid[i][j]
            else:
                top=dp[j] if i>0 else float('inf')
                left=dp[j-1] if j>0 else float('inf')
                dp[j]=grid[i][j]+min(top, left)
    return dp[-1]

print(min_path_sum_1([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
print(min_path_sum_2([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
print(min_path_sum_3([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
print(min_path_sum_4([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))