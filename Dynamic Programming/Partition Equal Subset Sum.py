#!/usr/bin/env python
# encoding: utf-8
"""
@author: dstch
@license: (C) Copyright 2013-2019, Regulus Tech.
@contact: dstch@163.com
@file: Partition Equal Subset Sum.py
@time: 2019/9/21 21:15
@desc: Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Note:

    Each of the array element will not exceed 100.
    The array size will not exceed 200.



Example 1:

Input: [1, 5, 11, 5]

Output: true

Explanation: The array can be partitioned as [1, 5, 5] and [11].



Example 2:

Input: [1, 2, 3, 5]

Output: false

Explanation: The array cannot be partitioned into equal sum subsets.

"""


class Solution:
    def canPartition(self, nums) -> bool:
        s = sum(nums)
        if s % 2 == 1:
            return False
        target = s >> 1
        dp = [False for _ in range(target + 1)]
        dp[0] = True
        for i in range(len(nums)):
            for j in range(nums[i], target + 1)[::-1]:
                dp[j] = dp[j] or dp[j - nums[i]]
        return dp[target]


if __name__ == '__main__':
    s = Solution()
    r = s.canPartition([1, 2, 3, 4, 5, 6, 7])
    print(r)
