# 198. House Robber
# You are a professional robber planning to rob houses along a street.Each house has a certain amount of money stashed,
# the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and
# it will automatically contact the police if two adjacent houses were broken into on the same night.
# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can
# rob tonight without alerting the police.

# Example 1:
# Input: nums = [1, 2, 3, 1]
# Output: 4
# Explanation: Rob house 1(money=1) and then rob house 3(money=3). Total amount you can rob = 1 + 3 = 4.

# Example 2:
# Input: nums = [2, 7, 9, 3, 1]
# Output: 12
# Explanation: Rob house # 1(money=2), rob house 3(money=9) and rob house 5(money=1). Total amount you can rob = 2 + 9 + 1 = 12.

# Constraints:
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 400

#Brute Force Recursion
def helper_1(nums, index):
    if index==0:
        return nums[index]
    if index<0:
        return 0
    return max(nums[index]+helper_1(nums, index-2), helper_1(nums, index-1))
def rob_1(nums):
    return helper_1(nums, len(nums)-1)

#Memoization
memo={}
def helper_2(nums, index):
    if index==0:
        return nums[index]
    if index<0:
        return 0
    if index in memo:
        return memo[index]
    memo[index]=max(nums[index]+helper_2(nums, index-2), helper_2(nums, index-1))
    return memo[index]
def rob_2(nums):
    return helper_2(nums, len(nums)-1)

#Tabulation
def rob_3(nums):
    n=len(nums)
    dp=[0]*(n)
    dp[0]=nums[0]
    dp[1]=max(nums[1], dp[0])
    for i in range(2, n):
        dp[i]=max(dp[i-1], nums[i]+dp[i-2])
    return dp[n-1]

#Space-Optimized Tabulation
def rob_4(nums):
    prev2=0
    prev1=0
    for i in range(0, len(nums)):
        curr=max(prev2+nums[i], prev1)
        prev2=prev1
        prev1=curr
    return prev1

print(rob_1([2, 7, 9, 3, 1]))
print(rob_2([2, 7, 9, 3, 1]))
print(rob_3([2, 7, 9, 3, 1]))
print(rob_4([2, 7, 9, 3, 1]))