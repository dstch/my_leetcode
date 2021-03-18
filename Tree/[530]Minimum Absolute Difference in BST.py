# Given a binary search tree with non-negative values, find the minimum absolute
#  difference between values of any two nodes. 
# 
#  Example: 
# 
#  
# Input:
# 
#    1
#     \
#      3
#     /
#    2
# 
# Output:
# 1
# 
# Explanation:
# The minimum absolute difference is 1, which is the difference between 2 and 1 
# (or between 2 and 3).
#  
# 
#  
# 
#  Note: 
# 
#  
#  There are at least two nodes in this BST. 
#  This question is the same as 783: https://leetcode.com/problems/minimum-dista
# nce-between-bst-nodes/ 
#  
#  Related Topics Tree 
#  👍 1161 👎 91


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        res = []

        def func(node):
            if node is None:
                return None
            func(node.left)
            res.append(node.val)
            func(node.right)

        func(root)
        m = 999999999999999999999
        for i, k in enumerate(res):
            if i + 1 == len(res):
                break
            t = abs(res[i] - res[i + 1])
            if m > t:
                m = t
        return m

# leetcode submit region end(Prohibit modification and deletion)
