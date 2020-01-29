'''
@Author: your name
@Date: 2020-01-29 11:54:36
@LastEditTime : 2020-01-29 12:23:01
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: \leetcode\322.coin-change.py
'''
#
# @lc app=leetcode id=322 lang=python
#
# [322] Coin Change
#

# @lc code=start


class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [amount+1]*(amount+1)
        dp[0] = 0
        for i in range(1, amount+1):
            for j in coins:
                if i>=j:
                    dp[i] = min(dp[i], dp[i-j]+1)
        if dp[-1] == amount+1:
            return -1
        else:
            return dp[-1]

# @lc code=end


if __name__ == "__main__":
    s = Solution()
    print(s.coinChange([1,2,5], 11))
