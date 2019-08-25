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
        self.quick_sort(g, 0, len(g) - 1)
        self.quick_sort(s, 0, len(s) - 1)
        i = j = res = 0
        while i < len(s) and j < len(g):
            if s[i] >= g[j]:
                res += 1
                j += 1
            i += 1
        return res

    def quick_sort(self, alist, start, end):
        if start >= end:
            return
        mid = alist[start]
        left = start
        right = end
        # left与right未重合，就向中间移动
        while left < right:
            while left < right and alist[right] >= mid:
                right -= 1
            alist[left] = alist[right]
            while left < right and alist[left] < mid:
                left += 1  # a_list = [1, 12, 22, 34, 21, 4, 6, 8, 11, 54, 36, 7, 3, 0, 60, 62, 63]
            alist[right] = alist[left]
        # 从循环退出后，left与right相遇，即left==right
        alist[left] = mid
        # 对左边部分执行快速排序
        self.quick_sort(alist, start, left - 1)
        # 对右边部分执行快速排序
        self.quick_sort(alist, left + 1, end)


if __name__ == '__main__':
    s = Solution()
    print(s.findContentChildren([10, 9, 8, 7], [5, 6, 7, 8]))
