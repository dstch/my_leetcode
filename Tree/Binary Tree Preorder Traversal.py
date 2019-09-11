#!/usr/bin/env python
# encoding: utf-8
"""
@author: dstch
@license: (C) Copyright 2013-2019, Regulus Tech.
@contact: dstch@163.com
@file: Binary Tree Preorder Traversal.py
@time: 2019/9/11 21:52
@desc: Given a binary tree, return the preorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return root
        s = [root]
        res = []
        while len(s) != 0:
            p = s[-1]
            s.pop()
            res.append(p.val)
            if p.right is not None:
                s.append(p.right)
            if p.left is not None:
                s.append(p.left)
        return res
