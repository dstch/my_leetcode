# The thief has found himself a new place for his thievery again. There is only 
# one entrance to this area, called the "root." Besides the root, each house has o
# ne and only one parent house. After a tour, the smart thief realized that "all h
# ouses in this place forms a binary tree". It will automatically contact the poli
# ce if two directly-linked houses were broken into on the same night. 
# 
#  Determine the maximum amount of money the thief can rob tonight without alert
# ing the police. 
# 
#  Example 1: 
# 
#  
# Input: [3,2,3,null,3,null,1]
# 
#      3
#     / \
#    2   3
#     \   \ 
#      3   1
# 
# Output: 7 
# Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7. 
# 
#  Example 2: 
# 
#  
# Input: [3,4,5,1,3,null,1]
# 
#      3
#     / \
#    4   5
#   / \   \ 
#  1   3   1
# 
# Output: 9
# Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.
#  Related Topics Dynamic Programming Tree Depth-first Search 
#  👍 3796 👎 65


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        dic = {}

        def dfs(node):
            if node is None:
                return 0
            if node in dic:
                return dic[node]
            result = node.val
            if node.left is not None:
                result += dfs(node.left.left) + dfs(node.left.right)
            if node.right is not None:
                result += dfs(node.right.left) + dfs(node.right.right)
            val = max(result, dfs(node.left) + dfs(node.right))
            dic[node] = val
            return val

        res = dfs(root)
        return res
# leetcode submit region end(Prohibit modification and deletion)
