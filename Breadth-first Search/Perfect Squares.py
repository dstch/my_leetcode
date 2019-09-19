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
        # Lagrange 四平方定理： 任何一个正整数都可以表示成不超过四个整数的平方之和。
        # 也就是说，这个题目返回的答案只有1、2、3、4这四种可能。 我们可以将输入的数字除以4来大大减少计算量，并不改变答案
        # 一个数除以8的余数，如果余数为7， 则其必然由四个完全平方数组成
        # 然后检测是否可以将简化后的数拆分为两个完全平方数，否则一定由三个完全平方数组成。
        import math
        while n % 4 == 0: n = n // 4
        if n % 8 == 7: return 4
        if int(math.sqrt(n)) ** 2 == n: return 1
        i = 1
        while i * i <= n:
            j = math.sqrt(n - i * i)
            if int(j) == j: return 2
            i += 1
        return 3


if __name__ == '__main__':
    s = Solution()
    s.numSquares(12)
