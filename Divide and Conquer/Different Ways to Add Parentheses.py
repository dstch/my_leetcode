#!/usr/bin/env python
# encoding: utf-8
"""
@author: dstch
@license: (C) Copyright 2013-2019, Regulus Tech.
@contact: dstch@163.com
@file: Different Ways to Add Parentheses.py
@time: 2019/8/31 10:30
@desc: Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. The valid operators are +, - and *.

Example 1:

Input: "2-1-1"
Output: [0, 2]
Explanation:
((2-1)-1) = 0
(2-(1-1)) = 2

Example 2:

Input: "2*3-4*5"
Output: [-34, -14, -10, -10, 10]
Explanation:
(2*(3-(4*5))) = -34
((2*3)-(4*5)) = -14
((2*(3-4))*5) = -10
(2*((3-4)*5)) = -10
(((2*3)-4)*5) = 10

"""


class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        fs = ['+', '-', '*']
        res = []
        if fs[0] not in input and fs[1] not in input and fs[2] not in input:
            return [int(input)]
        for index, n in enumerate(input):
            if n in fs:
                left = self.diffWaysToCompute(input[:index])
                right = self.diffWaysToCompute(input[index + 1:])
                for l in left:
                    for r in right:
                        res.append(self.cal_num(input[index], l, r))
        return res

    def cal_num(self, f, l, r):
        if f == '+':
            return l + r
        elif f == '-':
            return l - r
        else:
            return l * r


if __name__ == '__main__':
    s = Solution()
    print(s.diffWaysToCompute("2-1-1"))
