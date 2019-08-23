#!/usr/bin/env python
# encoding: utf-8
"""
@author: dstch
@license: (C) Copyright 2013-2019, Regulus Tech.
@contact: dstch@163.com
@file: Two Sum II - Input array is sorted.py
@time: 2019/8/23 9:17
@desc:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
"""


class Solution:
    def twoSum(self, numbers, target):
        """
        二分法
        :param numbers:
        :param target:
        :return:
        """
        l = len(numbers)
        for i in range(l):
            b = i
            e = l
            while b < e:
                j = (e + b) // 2
                r = numbers[i] + numbers[j]
                if r == target:
                    return [i + 1, j + 1]
                elif r > target:
                    e = j
                else:
                    b = j + 1

    def twoSum2(self, numbers, target):
        b = 0
        e = len(numbers) - 1
        while b != e:
            r = numbers[b] + numbers[e]
            if r == target:
                return [b + 1, e + 1]
            elif r < target:
                b += 1
            else:
                e -= 1


if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([2, 7, 11, 15], 9))
