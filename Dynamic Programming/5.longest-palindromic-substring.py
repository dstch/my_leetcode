'''
@Author: your name
@Date: 2020-01-28 11:34:03
@LastEditTime : 2020-01-28 11:54:41
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: \leetcode\5.longest-palindromic-substring.py
'''
#
# @lc app=leetcode id=5 lang=python
#
# [5] Longest Palindromic Substring
#

# @lc code=start


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 2:
            return s
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        max = 1
        start = 0
        for i in range(len(s)):
            dp[i][i] = True
            for j in range(0, i):
                dp[i][j] = ((i-j < 2 or dp[i-1][j+1]) and s[i] == s[j])
                if dp[i][j] and max < i-j+1:
                    max = i-j+1
                    start = j
        return s[start:start+max]
# @lc code=end


if __name__ == '__main__':
    s = Solution()
    s.longestPalindrome('ac')
