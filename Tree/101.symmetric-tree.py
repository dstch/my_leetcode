'''
Author: your name
Date: 2021-02-14 23:24:28
LastEditTime: 2021-02-14 23:46:59
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \my_leetcode\Tree\101.symmetric-tree.py
'''
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
        def func(node1, node2):
            if node1 is None and node2 is None:
                return True
            if node1 is None or node2 is None:
                return False
            if node1.val != node2.val:
                return False
            return func(node1.left, node2.right) and func(node1.right, node2.left)
        if root is None:
            return True
        return func(root.left, root.right)

# @lc code=end
