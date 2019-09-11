#!/usr/bin/env python
# encoding: utf-8
"""
@author: dstch
@license: (C) Copyright 2013-2019, Regulus Tech.
@contact: dstch@163.com
@file: Find Bottom Left Tree Value.py
@time: 2019/9/11 21:05
@desc:  Given a binary tree, find the leftmost value in the last row of the tree.

Example 1:

Input:

    2
   / \
  1   3

Output:
1

Example 2:

Input:

        1
       / \
      2   3
     /   / \
    4   5   6
       /
      7

Output:
7

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        q = [root]
        res = -1
        while len(q) > 0:
            n = len(q)
            for i in range(n):
                p = q[0]
                q.pop()
                if i == 0:
                    res = p.val
                if p.left is not None:
                    q.append(p.left)
                if p.right is not None:
                    q.append(p.right)
        return res
