# 1137. N-th Tribonacci Number
# The Tribonacci sequence Tn is defined as follows:
# T0 = 0, T1 = 1, T2 = 1, and Tn + 3 = Tn + Tn + 1 + Tn + 2 for n >= 0.
# Given n, return the value of Tn.
# Example 1:
# Input: n = 4
# Output: 4
# Explanation:
# T_3 = 0 + 1 + 1 = 2
# T_4 = 1 + 1 + 2 = 4
# Example 2:
# Input: n = 25
# Output: 1389537
# Constraints:
# 0 <= n <= 37
# The answer is guaranteed to fit within a 32 - bit integer, ie.answer <= 2 ^ 31 - 1.

#Brute Force Recursion
def tribonacci_1(n):
    if n==0:
        return 0
    if n==1 or n==2:
        return 1
    return tribonacci_1(n-1)+tribonacci_1(n-2)+tribonacci_1(n-3)

#Memoization
memo={}
def tribonacci_2(n):
    if n==0:
        return 0
    if n==1 or n==2:
        return 1
    if n in memo:
        return memo[n]
    memo[n]=tribonacci_2(n-1)+tribonacci_2(n-2)+tribonacci_2(n-3)
    return memo[n]

#Tabulation
def tribonacci_3(n):
    dp=[0]*(n+1)
    dp[1]=1
    dp[2]=1
    for i in range(3, n+1):
        dp[i]=dp[i-1]+dp[i-2]+dp[i-3]
    return dp[n]

#Space-Optimized Tabulation
def tribonacci_4(n):
    if n==0:
        return 0
    if n==1 or n==2:
        return 1
    a, b, c=0, 1, 1
    for i in range(3, n+1):
        a, b, c=b, c, a+b+c
    return c
print(tribonacci_1(3))
print(tribonacci_2(3))
print(tribonacci_3(3))
print(tribonacci_4(3))