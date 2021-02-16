'''
Author: your name
Date: 2021-02-15 16:56:54
LastEditTime: 2021-02-16 22:31:52
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \my_leetcoded:\code\leetcode\103.binary-tree-zigzag-level-order-traversal.py
'''
#
# @lc app=leetcode id=103 lang=python
#
# [103] Binary Tree Zigzag Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []

        def func(node, level):
            if len(res) == level:
                res.append([])
            if node is not None:
                res[level].append(node.val)
                if node.left is not None:
                    func(node.left, level+1)
                if node.right is not None:
                    func(node.right, level+1)
        if root is None:
            return []
        func(root, 0)
        for x in range(len(res)):
            if x % 2 != 0:
                res[x] = res[x][::-1]
        return res

# @lc code=end
