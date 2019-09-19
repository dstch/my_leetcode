#!/usr/bin/env python
# encoding: utf-8
"""
@author: dstch
@license: (C) Copyright 2013-2019, Regulus Tech.
@contact: dstch@163.com
@file: Redundant Connection.py
@time: 2019/9/18 16:42
@desc:  In this problem, a tree is an undirected graph that is connected and has no cycles.

The given input is a graph that started as a tree with N nodes (with distinct values 1, 2, ..., N), with one additional edge added. The added edge has two different vertices chosen from 1 to N, and was not an edge that already existed.

The resulting graph is given as a 2D-array of edges. Each element of edges is a pair [u, v] with u < v, that represents an undirected edge connecting nodes u and v.

Return an edge that can be removed so that the resulting graph is a tree of N nodes. If there are multiple answers, return the answer that occurs last in the given 2D-array. The answer edge [u, v] should be in the same format, with u < v.

Example 1:

Input: [[1,2], [1,3], [2,3]]
Output: [2,3]
Explanation: The given undirected graph will be like this:
  1
 / \
2 - 3

Example 2:

Input: [[1,2], [2,3], [3,4], [1,4], [1,5]]
Output: [1,4]
Explanation: The given undirected graph will be like this:
5 - 1 - 2
    |   |
    4 - 3

"""
import collections


class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        tree = [-1] * (len(edges) + 1)  # 保存的是每个点的上级，最后会变成每个点的根节点
        for edge in edges:
            a = self.find_root(tree, edge[0])
            b = self.find_root(tree, edge[1])
            if a != b:
                tree[a] = b
            else:
                return edge

    def find_root(self, tree, root):
        if tree[root] == -1:
            return root
        else:
            temp_root = self.find_root(tree, tree[root])
            tree[root] = temp_root  # 压缩路径
            return temp_root
