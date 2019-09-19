#!/usr/bin/env python
# encoding: utf-8
"""
@author: dstch
@license: (C) Copyright 2013-2019, Regulus Tech.
@contact: dstch@163.com
@file: Minimum Path Sum.py
@time: 2019/9/19 22:45
@desc: Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.


"""


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        paths = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j == 0:
                    paths[i][j] = grid[i][j]
                elif i == 0:
                    paths[i][j] = grid[i][j] + paths[i][j - 1]
                elif j == 0:
                    paths[i][j] = grid[i][j] + paths[i - 1][j]
                else:
                    paths[i][j] = min(grid[i][j] + paths[i - 1][j], grid[i][j] + paths[i][j - 1])
        return paths[-1][-1]
