'''
@Author: your name
@Date: 2020-01-29 20:13:33
@LastEditTime : 2020-01-29 20:24:57
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: \leetcode\136.single-number.py
'''
#
# @lc app=leetcode id=136 lang=python
#
# [136] Single Number
#

# @lc code=start


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num = nums[0]
        for n in nums[1:]:
            num = num ^ n
        return num
# @lc code=end
