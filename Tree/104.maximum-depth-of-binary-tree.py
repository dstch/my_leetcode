'''
Author: your name
Date: 2021-02-16 22:34:06
LastEditTime: 2021-02-16 22:45:20
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \my_leetcoded:\code\leetcode\104.maximum-depth-of-binary-tree.py
'''
#
# @lc app=leetcode id=104 lang=python
#
# [104] Maximum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        res=[]
        def func(node,level):
            if len(res)==level:
                res.append([])
            if node is not None:
                # res[level].append(node.val)
                if node.left is not None:
                    func(node.left,level+1)
                if node.right is not None:
                    func(node.right,level+1)
        func(root,0)
        return len(res) 
        
# @lc code=end

