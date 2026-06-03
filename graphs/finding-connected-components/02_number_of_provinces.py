# 547. Number of Provinces
# There are n cities.Some of them are connected, while some are not.If city a is connected directly with city b, and
# city b is connected directly with city c, then city a is connected indirectly with city c. A province is a group of
# directly or indirectly connected cities and no other cities outside of the group. You are given an n x n matrix
# isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and
# isConnected[i][j] = 0 otherwise. Return the total number of provinces.

# Example 1:
# Input: isConnected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
# Output: 2

# Example 2:
# Input: isConnected = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
# Output: 3

# Constraints:
# 1 <= n <= 200
# n == isConnected.length
# n == isConnected[i].length
# isConnected[i][j] is 1 or 0.
# isConnected[i][i] == 1
# isConnected[i][j] == isConnected[j][i]

# Depth-First Search By Recursion
def dfs_1(src, isConnected, vis):
    vis[src] = 1
    for i in range(len(isConnected)):
        if isConnected[src][i] == 1 and vis.get(i) != 1:
            dfs_1(i, isConnected, vis)

def number_of_provinces_1(isConnected):
    vis = dict()
    provinces = 0
    for city in range(len(isConnected)):
        if city not in vis:
            provinces += 1
            dfs_1(city, isConnected, vis)
    return provinces

# Depth-First Search By Stack
def dfs_2(src, isConnected, vis):
    nodes=[]
    vis[src] = 1
    nodes.append(src)
    while len(nodes)!=0:
        currNode=nodes.pop()
        for i in range(len(isConnected)):
            if isConnected[currNode][i] == 1 and vis.get(i) != 1:
                vis[i]=1
                nodes.append(i)

def number_of_provinces_2(isConnected):
    vis = dict()
    provinces = 0
    for city in range(len(isConnected)):
        if city not in vis:
            provinces += 1
            dfs_2(city, isConnected, vis)
    return provinces

isConnected = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
print(number_of_provinces_1(isConnected))
print(number_of_provinces_2(isConnected))