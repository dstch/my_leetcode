#!/usr/bin/env python
# encoding: utf-8
"""
@author: dstch
@license: (C) Copyright 2013-2019, Regulus Tech.
@contact: dstch@163.com
@file: Assign Cookies.py
@time: 2019/8/24 14:57
@desc: Input: [1,2,3], [1,1]

Output: 1

Explanation: You have 3 children and 2 cookies. The greed factors of 3 children are 1, 2, 3.
And even though you have 2 cookies, since their size is both 1, you could only make the child whose greed factor is 1 content.
You need to output 1.
"""


class Solution:
    def findContentChildren(self, g, s) -> int:
        g = self.sorted(g)
        s = self.sorted(s)
        i = j = res = 0
        while i < len(s) and j < len(g):
            if s[i] >= g[j]:
                res += 1
                j += 1
            i += 1
        return res

    def sorted(self, nums):
        for i in range(0, len(nums) - 1):
            for j in range(1, len(nums) - i):
                if nums[j - 1] > nums[j]:
                    nums[j - 1], nums[j] = nums[j], nums[j - 1]
        return nums


if __name__ == '__main__':
    s = Solution()
    print(s.findContentChildren([10, 9, 8, 7], [5, 6, 7, 8]))
