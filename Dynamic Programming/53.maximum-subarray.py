'''
@Author: your name
@Date: 2020-01-28 22:17:20
@LastEditTime : 2020-01-28 22:24:29
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: \leetcode\53.maximum-subarray.py
'''
#
# @lc app=leetcode id=53 lang=python
#
# [53] Maximum Subarray
#

# @lc code=start


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1]+nums[i], nums[i])
        return max(dp)
# @lc code=end
