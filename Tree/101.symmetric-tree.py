#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def func(node, result):
            if node is not None:

                func(node.left, result)
                result.append(node.val)
                func(node.right, result)

        def func1(node, result):
            if node is not None:
                func1(node.right, result)
                result.append(node.val)
                func1(node.left, result)
                
                
        left, right = [], []
        func(root.left, left)
        func1(root.right, right)
        return left == right

# @lc code=end
