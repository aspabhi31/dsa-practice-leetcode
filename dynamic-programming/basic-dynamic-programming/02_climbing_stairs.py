# 70. Climbing Stairs
# You are climbing a staircase.It takes n steps to reach the top. Each time you can either climb 1 or 2 steps.In how
# many distinct ways can you climb to the top?
# Example 1:
# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:
# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
# Constraints:
# 1 <= n <= 45

#Brute Force Recursion
def climbing_stairs_1(n):
    if n==0:
        return 1
    if n<0:
        return 0
    return climbing_stairs_1(n-1)+climbing_stairs_1(n-2)
#Memoization
memo={}
def climbing_stairs_2(n):
    if n==0:
        return 1
    if n<0:
        return 0
    if n in memo:
        return memo[n]
    memo[n]=climbing_stairs_2(n-1)+climbing_stairs_2(n-2)
    return memo[n]
#Tabulation
def climbing_stairs_3(n):
    dp=[0]*(n+1)
    dp[0]=1
    for i in range(1, n+1):
        if i==1:
            dp[i]=dp[i-1]
            continue
        dp[i]=dp[i-1]+dp[i-2]
    return dp[n]
#Space-Optimized Tabulation
def climbing_stairs_4(n):
    if n==0:
        return 1
    prev2=1#f(0)
    prev1=1#f(1)
    for i in range(2, n+1):
        curr=prev2+prev1
        prev2=prev1
        prev1=curr
    return prev1
print(climbing_stairs_1(3))
print(climbing_stairs_2(3))
print(climbing_stairs_3(3))
print(climbing_stairs_4(3))