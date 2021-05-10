# Given two strings text1 and text2, return the length of their longest common s
# ubsequence. If there is no common subsequence, return 0. 
# 
#  A subsequence of a string is a new string generated from the original string 
# with some characters (can be none) deleted without changing the relative order o
# f the remaining characters. 
# 
#  
#  For example, "ace" is a subsequence of "abcde". 
#  
# 
#  A common subsequence of two strings is a subsequence that is common to both s
# trings. 
# 
#  
#  Example 1: 
# 
#  
# Input: text1 = "abcde", text2 = "ace" 
# Output: 3  
# Explanation: The longest common subsequence is "ace" and its length is 3.
#  
# 
#  Example 2: 
# 
#  
# Input: text1 = "abc", text2 = "abc"
# Output: 3
# Explanation: The longest common subsequence is "abc" and its length is 3.
#  
# 
#  Example 3: 
# 
#  
# Input: text1 = "abc", text2 = "def"
# Output: 0
# Explanation: There is no such common subsequence, so the result is 0.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= text1.length, text2.length <= 1000 
#  text1 and text2 consist of only lowercase English characters. 
#  
#  Related Topics Dynamic Programming 
#  👍 2998 👎 38


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        mono = []
        for i in range(len(text1)):
            mono.append([-1] * len(text2))

        def dp(t1, i, t2, j):
            if i == len(t1) or j == len(t2):
                return 0
            if mono[i][j] != -1:
                return mono[i][j]
            if t1[i] == t2[j]:
                mono[i][j] = 1 + dp(t1, i + 1, t2, j + 1)
            else:
                mono[i][j] = max(
                    dp(t1, i + 1, t2, j),
                    dp(t1, i, t2, j + 1)
                )
            return mono[i][j]

        res = dp(text1, 0, text2, 0)
        return res


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    # s = Solution()
    # s.longestCommonSubsequence("bl", "yby")
    mono = []
    for i in range(3):
        mono.append([-1] * 3)
    print(mono)
    mono[0][0] = 1
    print(mono)
