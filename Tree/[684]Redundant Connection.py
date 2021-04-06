# 
# In this problem, a tree is an undirected graph that is connected and has no cy
# cles.
#  
# The given input is a graph that started as a tree with N nodes (with distinct 
# values 1, 2, ..., N), with one additional edge added. The added edge has two dif
# ferent vertices chosen from 1 to N, and was not an edge that already existed.
#  
# The resulting graph is given as a 2D-array of edges. Each element of edges is 
# a pair [u, v] with u < v, that represents an undirected edge connecting nodes u 
# and v.
#  
# Return an edge that can be removed so that the resulting graph is a tree of N 
# nodes. If there are multiple answers, return the answer that occurs last in the 
# given 2D-array. The answer edge [u, v] should be in the same format, with u < v.
# 
#  Example 1: 
#  
# Input: [[1,2], [1,3], [2,3]]
# Output: [2,3]
# Explanation: The given undirected graph will be like this:
#   1
#  / \
# 2 - 3
#  
#  
#  Example 2: 
#  
# Input: [[1,2], [2,3], [3,4], [1,4], [1,5]]
# Output: [1,4]
# Explanation: The given undirected graph will be like this:
# 5 - 1 - 2
#     |   |
#     4 - 3
#  
#  
#  Note: 
#  The size of the input 2D-array will be between 3 and 1000. 
#  Every integer represented in the 2D-array will be between 1 and N, where N is
#  the size of the input array. 
#  
# 
#  
# 
#  
# Update (2017-09-26): 
# We have overhauled the problem description + test cases and specified clearly 
# the graph is an undirected graph. For the directed graph follow up please see Re
# dundant Connection II). We apologize for any inconvenience caused.
#  Related Topics Tree Union Find Graph 
#  👍 1988 👎 246


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # 解题思路：本题是从一个图中找出删去一个边就能变成树
        # 所以只要找到边的两个节点都属于同一个根节点即可
        def find_root(root):
            if tree[root] == -1:
                return root
            else:
                temp_root = find_root(tree[root])
                tree[root] = temp_root  # 压缩路径
                return temp_root

        tree = [-1] * (len(edges) + 1)  # 这里tree能这么声明是因为题目本身节点数值的大小跟长度是相关的
        for edgs in edges:
            a = find_root(edgs[0])
            b = find_root(edgs[1])
            if a == b:
                return edgs
            else:
                tree[a] = b  # 同根

# leetcode submit region end(Prohibit modification and deletion)
