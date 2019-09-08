#!/usr/bin/env python
# encoding: utf-8
"""
@author: dstch
@license: (C) Copyright 2013-2019, Regulus Tech.
@contact: dstch@163.com
@file: Single Number III.py
@time: 2019/9/7 22:09
@desc: Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

Example:

Input:  [1,2,1,3,2,5]
Output: [3,5]
"""


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sum = 0
        num1 = 0
        num2 = 0
        for n in nums:
            sum = sum ^ n
        mask = 1
        while sum & mask == 0:
            mask = mask << 1
        for n in nums:
            if n & mask == 0:
                num1 = num1 ^ n
            else:
                num2 = num2 ^ n
        return [num1, num2]


if __name__ == '__main__':
    s = Solution()
    s.singleNumber([1, 1, 2])
