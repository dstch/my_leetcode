#!/usr/bin/env python
# encoding: utf-8
"""
@author: dstch
@license: (C) Copyright 2013-2019, Regulus Tech.
@contact: dstch@163.com
@file: Longest Increasing Subsequence.py
@time: 2019/9/20 22:35
@desc: Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
"""


class Solution:
    def lengthOfLIS(self, nums: list) -> int:
        if len(nums) == 0:
            return 0
        dp = [1 for _ in range(len(nums))]
        m = 1
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[j] + 1, dp[i])
                    m = max(m, dp[i])
        return m


if __name__ == '__main__':
    s = Solution()
    s.lengthOfLIS([10, 22, 9, 33, 21, 50, 41, 60, 80])
