#!/usr/bin/env python
# encoding: utf-8
"""
@author: dstch
@license: (C) Copyright 2013-2019, Regulus Tech.
@contact: dstch@163.com
@file: Sqrt(x).py
@time: 2019/8/28 11:40
@desc: Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:

Input: 4
Output: 2

Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since
             the decimal part is truncated, 2 is returned.
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        result = x
        while result > x / result:
            result = int(result - 0.5 * (result - x / result))
        return int(result)


if __name__ == '__main__':
    s = Solution()
    print(s.mySqrt(7))
