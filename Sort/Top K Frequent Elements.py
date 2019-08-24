#!/usr/bin/env python
# encoding: utf-8
"""
@author: dstch
@license: (C) Copyright 2013-2019, Regulus Tech.
@contact: dstch@163.com
@file: Top K Frequent Elements.py
@time: 2019/8/24 12:43
@desc: Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:

Input: nums = [1], k = 1
Output: [1]
"""


class Solution:
    def topKFrequent(self, nums, k: int):
        dic = {}
        for n in nums:
            if n in dic:
                dic[n] += 1
            else:
                dic[n] = 1
        bucket = [[] for i in range(len(nums) + 1)]
        for key in dic:
            bucket[dic[key]].append(key)
        res = []
        for i in bucket[::-1]:
            res.extend(i)
            if len(res) >= k:
                break
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.topKFrequent([1, 1, 1, 2, 2, 3], 2))
