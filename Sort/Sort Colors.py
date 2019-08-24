#!/usr/bin/env python
# encoding: utf-8
"""
@author: dstch
@license: (C) Copyright 2013-2019, Regulus Tech.
@contact: dstch@163.com
@file: Sort Colors.py
@time: 2019/8/24 13:24
@desc: Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
"""


class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red = white = 0
        blue = len(nums) - 1
        while white <= blue:
            if nums[white] == 1:
                white += 1
            elif white >= red and nums[white] == 0:
                if nums[red] != 0:
                    nums[white], nums[red] = nums[red], nums[white]
                white += 1
                red += 1
            elif white <= blue and nums[white] == 2:
                if nums[blue] != 2:
                    nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1


if __name__ == '__main__':
    s = Solution()
    print(s.sortColors([2, 0, 2, 1, 1, 0]))
