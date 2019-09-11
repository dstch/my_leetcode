#!/usr/bin/env python
# encoding: utf-8
"""
@author: dstch
@license: (C) Copyright 2013-2019, Regulus Tech.
@contact: dstch@163.com
@file: Kth Smallest Element in a BST.py
@time: 2019/9/11 22:08
@desc: Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note:
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Example 1:

Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1

Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# BST中序遍历后是一个有序数组
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        return self.get_list(root, [])[k]

    def get_list(self, root, res):
        if root.left is not None:
            res = self.get_list(root.left, res)
        if root is not None:
            res.append(root.val)
        if root.right is not None:
            res = self.get_list(root.right, res)
        return res


# 分治思想
class Solution1:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        cnt = self.count(root.left)
        if k <= cnt:
            return self.kthSmallest(root.left, k)
        elif k > cnt + 1:
            return self.kthSmallest(root.right, k - cnt - 1)
        return root.val

    def count(self, root):
        if root is None:
            return 0
        return 1 + self.count(root.left) + self.count(root.right)
