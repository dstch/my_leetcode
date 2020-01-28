'''
@Author: your name
@Date: 2020-01-28 17:30:35
@LastEditTime : 2020-01-28 18:34:25
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: \leetcode\72.edit-distance.py
'''
#
# @lc app=leetcode id=72 lang=python
#
# [72] Edit Distance
#

# @lc code=start


class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        edit = [[i+j for j in range(len(word2)+1)]
                for i in range(len(word1)+1)]
        for i in range(1, len(word1)+1):
            for j in range(1, len(word2)+1):
                edit[i][j] = min(edit[i-1][j]+1, edit[i][j-1]+1,
                                 edit[i-1][j-1] + (0 if word1[i-1] == word2[j-1] else 1))
        return edit[len(word1)][len(word2)]
# @lc code=end


if __name__ == '__main__':
    s = Solution()
    result = s.minDistance('', '')
    print(result)
