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
        l = 0
        r = len(nums) - 1
        key = len(nums) - k
        mid = self.partition(nums, l, r)
        while mid != key:
            if mid < key:
                mid = self.partition(nums, mid + 1, r)
            else:
                mid = self.partition(nums, l, mid - 1)
        return nums[mid]

    def partition(self, nums, l, r):
        p = nums[l]
        while l < r:
            while l < r and p <= nums[r]:
                r -= 1
            nums[l] = nums[r]
            while l < r and p >= nums[l]:
                l += 1
            nums[r] = nums[l]
        nums[r] = p
        return l


if __name__ == '__main__':
    s = Solution()
    print(s.findKthLargest([2, 1], 1))
