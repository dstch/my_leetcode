#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import sys


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def func(root, min_val, max_val):
            if root is None:
                return True
            elif root.val <= min_val or root.val >= max_val:
                return False
            return func(root.left, min_val, root.val) and func(root.right, root.val, max_val)
        return func(root, -sys.maxsize-1, sys.maxsize)

# @lc code=end
