#!/usr/bin/env python
# encoding: utf-8
"""
@author: dstch
@license: (C) Copyright 2013-2019, Regulus Tech.
@contact: dstch@163.com
@file: Range Sum Query - Immutable.py
@time: 2019/9/19 23:44
@desc: Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Example:

Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3

"""


class NumArray:

    def __init__(self, nums: List[int]):
        n = len(nums)
        self.matrix = [[0 for x in range(n)] for _ in range(n)]
        for i in range(n-1):
            for j in range(n)[i:]:
                self.matrix[i][j]=self.matrix[i]

    def sumRange(self, i: int, j: int) -> int:
        res = 0
        for i in self.l[i:j]:
            res += i
        return res
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
