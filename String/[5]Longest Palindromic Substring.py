# Given a string s, return the longest palindromic substring in s. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
#  
# 
#  Example 2: 
# 
#  
# Input: s = "cbbd"
# Output: "bb"
#  
# 
#  Example 3: 
# 
#  
# Input: s = "a"
# Output: "a"
#  
# 
#  Example 4: 
# 
#  
# Input: s = "ac"
# Output: "a"
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 1000 
#  s consist of only digits and English letters (lower-case and/or upper-case), 
# 
#  Related Topics String Dynamic Programming 
#  👍 10467 👎 679


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def func(s, l, r):
            while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l + 1:r]

        res = ""
        for i in range(len(s)):
            a = func(s, i, i)
            b = func(s, i, i + 1)
            if len(a) > len(res):
                res = a
            if len(b) > len(res):
                res = b
        return res


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    s = Solution()
    s.longestPalindrome('bb')
