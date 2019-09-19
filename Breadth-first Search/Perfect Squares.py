#!/usr/bin/env python
# encoding: utf-8
"""
@author: dstch
@license: (C) Copyright 2013-2019, Regulus Tech.
@contact: dstch@163.com
@file: Perfect Squares.py
@time: 2019/9/19 15:25
@desc: Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.

Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
"""


class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        q = [[n, 0]]
        visited = [False for _ in range(n + 1)]
        while any(q):
            i = 1
            num, step = q.pop(0)
            tnum = num - i ** 2
            while tnum >= 0:
                if tnum == 0:
                    return step + 1
                if visited[tnum] == False:
                    visited[tnum] = True
                    q.append([tnum, step + 1])
                i += 1
                tnum = num - i ** 2
