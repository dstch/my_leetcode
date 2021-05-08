# Given a string s, find the length of the longest substring without repeating c
# haracters. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
#  
# 
#  Example 2: 
# 
#  
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
#  
# 
#  Example 3: 
# 
#  
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a 
# substring.
#  
# 
#  Example 4: 
# 
#  
# Input: s = ""
# Output: 0
#  
# 
#  
#  Constraints: 
# 
#  
#  0 <= s.length <= 5 * 104 
#  s consists of English letters, digits, symbols and spaces. 
#  
#  Related Topics Hash Table Two Pointers String Sliding Window 
#  👍 14247 👎 733


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        res = [s[0]]
        dic = {s[0]: 0}
        left, right = 0, 1
        length = 1
        while len(s) > right > left:
            if s[right] in res:  # 出现重复
                left = dic[s[right]] + 1
                dic[s[right]] = right
                res.clear()
                right += 1
                res.extend([x for x in s[left:right]])
            else:
                length = max(length, right - left + 1)
                res.append(s[right])
                dic[s[right]] = right
                right += 1
        return length


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    s = 'abcabcbb'
    ss = Solution()
    a = ss.lengthOfLongestSubstring(s)
    print(a)
