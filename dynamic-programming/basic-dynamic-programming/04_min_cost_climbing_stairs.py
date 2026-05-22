# 746. Min Cost Climbing Stairs
# You are given an integer array cost where cost[i] is the cost of ith step on a staircase.Once you pay the cost, you
# can either climb one or two steps. You can either start from the step with index 0, or the step with index 1. Return
# the minimum cost to reach the top of the floor.
# Example 1:
# Input: cost = [10, 15, 20]
# Output: 15
# Explanation: You will start at index 1. - Pay 15 and climb two steps to reach the top. The total cost is 15.
# Example 2:
# Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
# Output: 6
# Explanation: You will start at index 0. - Pay 1 and climb two steps to reach index 2. - Pay 1 and climb two steps to
# reach index 4. - Pay 1 and climb two steps to reach index 6. - Pay 1 and climb one step to reach index 7. -Pay 1 and
# climb two steps to reach index 9. - Pay 1 and climb one step to reach the top. The total cost is 6.
# Constraints:
# 2 <= cost.length <= 1000
# 0 <= cost[i] <= 999

#Brute Force Recursion
cost=[]
def helper_1(index):
    global cost
    if index>=len(cost):
        return 0
    return cost[index]+min(helper_1(index+1), helper_1(index+2))
def min_cost_1(cost_local):
    global cost
    cost=cost_local
    return min(helper_1(0), helper_1(1))

#Memoization
memo={}
def helper_2(index):
    global cost
    if index>=len(cost):
        return 0
    if index in memo:
        return memo[index]
    memo[index]=cost[index]+min(helper_2(index+1), helper_2(index+2))
    return memo[index]
def min_cost_2(cost_local):
    global cost
    cost=cost_local
    return min(helper_2(0), helper_2(1))

#Tabulation
def min_cost_3(cost):
    n=len(cost)
    dp=[0]*(n+1)
    for i in range(2, n+1):
        one_step=dp[i-1]+cost[i-1]
        two_step=dp[i-2]+cost[i-2]
        dp[i]=min(one_step, two_step)
    return dp[n]

#Space Optimized Tabulation
def min_cost_4(cost):
    prev2=0
    prev1=0
    for i in range(2, len(cost)+1):
        curr=min(prev2+cost[i-2], prev1+cost[i-1])
        prev2=prev1
        prev1=curr
    return prev1

print(min_cost_1([10, 15, 20]))
print(min_cost_2([10, 15, 20]))
print(min_cost_3([10, 15, 20]))
print(min_cost_4([10, 15, 20]))