'''
Author: your name
Date: 2021-02-15 16:23:59
LastEditTime: 2021-02-15 16:53:26
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \my_leetcoded:\code\leetcode\102.binary-tree-level-order-traversal.py
'''
#
# @lc app=leetcode id=102 lang=python
#
# [102] Binary Tree Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        def func(node, level):
            if len(res)==level:
                res.append([])

            if node is not None:
                res[level].append(node.val)
            if node.left is not None:
                func(node.left,level+1)
            if node.right is not None:
                func(node.right,level+1)
        
        if root is None:
            return []
        func(root,0)
        return res
# @lc code=end
