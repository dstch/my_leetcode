#!/usr/bin/env python
# encoding: utf-8
"""
@author: dstch
@license: (C) Copyright 2013-2019, Regulus Tech.
@contact: dstch@163.com
@file: Base 7.py
@time: 2019/9/7 22:25
@desc: Given an integer, return its base 7 string representation.

Example 1:

Input: 100
Output: "202"

Example 2:

Input: -7
Output: "-10"

"""


class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        s = ''
        r = ''
        if num < 0:
            r = '-'
            num = -num
        while num >= 7:
            s += str(num % 7)
            num //= 7
        s += str(num)
        s = r + s[::-1]
        return s


if __name__ == '__main__':
    s = Solution()
    print(s.convertToBase7(-7))
