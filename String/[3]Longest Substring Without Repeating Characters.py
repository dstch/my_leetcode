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
        """
        使用滑动窗口解题
        窗口的右边界就是当前遍历到的字符的位置，为了求出窗口的大小，我们需要一个变量 left 来指向滑动窗口的左边界，这样，如果当前遍历到的字符从未出现过，那么直接扩大右边界，如果之前出现过，那么就分两种情况，在或不在滑动窗口内，如果不在滑动窗口内，当前字符可以直接加进来，如果在的话，就需要先在滑动窗口内去掉这个已经出现过的字符，去掉的方法并不需要将左边界 left 一位一位向右遍历查找，由于我们的 int[] 已经保存了该重复字符最后出现的位置，所以直接移动 left 指针就可以了。我们维护一个结果 res，每次用出现过的窗口大小来更新结果 res，就可以得到最终结果了。
        其实我们并不需要判断当前字符是否已经在滑动窗口中出现，只要我们每遍历一个字符，保证 left = Math.max(left, m[s.charAt(i)]) 即可，相当于执行上面所述的判断操作。
        """
        sub = ""
        res = 0
        for i in s:
            if i not in sub:
                sub += i
                res = max(res, len(sub))
            else:
                sub += i
                sub = sub[sub.index(i) + 1:]
        return res
    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     if not s:
    #         return 0
    #     res = [s[0]]
    #     dic = {s[0]: 0}
    #     left, right = 0, 1
    #     length = 1
    #     while len(s) > right > left:
    #         if s[right] in res:  # 出现重复
    #             left = dic[s[right]] + 1
    #             dic[s[right]] = right
    #             res.clear()
    #             right += 1
    #             res.extend([x for x in s[left:right]])
    #         else:
    #             length = max(length, right - left + 1)
    #             res.append(s[right])
    #             dic[s[right]] = right
    #             right += 1
    #     return length


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    s = 'abcabcbb'
    ss = Solution()
    a = ss.lengthOfLongestSubstring(s)
    print(a)
