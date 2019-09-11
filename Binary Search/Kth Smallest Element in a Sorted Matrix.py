#!/usr/bin/env python
# encoding: utf-8
"""
@author: dstch
@license: (C) Copyright 2013-2019, Regulus Tech.
@contact: dstch@163.com
@file: Kth Smallest Element in a Sorted Matrix.py
@time: 2019/9/4 20:41
@desc: Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.

"""


class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        l = matrix[0][0]
        r = matrix[-1][-1]
        while l <= r:
            mid = (l + r) // 2
            cnt = self.search(matrix, mid)
            if cnt < k:
                l = mid + 1
            else:
                r = mid - 1
        return l

    def search(self, matrix, mid):
        cnt = 0
        n = len(matrix)
        for i in range(n):
            if mid > matrix[i][-1]:
                cnt += n
            else:
                for j in range(n):
                    if mid >= matrix[i][j]:
                        cnt += 1
        return cnt


class Solution1(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        lo, hi = matrix[0][0], matrix[-1][-1]
        while lo <= hi:
            mid = (lo + hi) >> 1
            loc = self.countLower(matrix, mid)
            if loc >= k:
                hi = mid - 1
            else:
                lo = mid + 1
        return lo

    def countLower(self, matrix, num):
        i, j = len(matrix) - 1, 0
        cnt = 0
        while i >= 0 and j < len(matrix[0]):
            if matrix[i][j] <= num:
                cnt += i + 1
                j += 1
            else:
                i -= 1
        return cnt


if __name__ == '__main__':
    s = Solution()
    print(s.kthSmallest([[1, 2], [1, 3]], 3))
