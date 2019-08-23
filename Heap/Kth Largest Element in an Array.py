#!/usr/bin/env python
# encoding: utf-8
"""
@author: dstch
@license: (C) Copyright 2013-2019, Regulus Tech.
@contact: dstch@163.com
@file: Kth Largest Element in an Array.py
@time: 2019/8/23 11:28
@desc:
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:
Input: [3,2,1,5,6,4] and k = 2
Output: 5

Example 2:
Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
"""


class Solution:
    def findKthLargest(self, nums, k) -> int:
        i = 0

        while len(nums) != 0:
            pi = len(nums) // 2
            p = nums[pi]
            left, right, i = self.partition(nums, p)
            if k < i:
                nums = left
            else:
                nums = right
        return p

    def partition(self, nums, p):
        left = []
        right = []
        for i in range(len(nums)):
            if nums[i] > p:
                left.append(nums[i])
            elif nums[i] < p:
                right.append(nums[i])
        return left, right, len(left)


if __name__ == '__main__':
    s = Solution()
    print(s.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
