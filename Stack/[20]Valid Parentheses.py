# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']
# ', determine if the input string is valid. 
# 
#  An input string is valid if: 
# 
#  
#  Open brackets must be closed by the same type of brackets. 
#  Open brackets must be closed in the correct order. 
#  
# 
#  
#  Example 1: 
# 
#  
# Input: s = "()"
# Output: true
#  
# 
#  Example 2: 
# 
#  
# Input: s = "()[]{}"
# Output: true
#  
# 
#  Example 3: 
# 
#  
# Input: s = "(]"
# Output: false
#  
# 
#  Example 4: 
# 
#  
# Input: s = "([)]"
# Output: false
#  
# 
#  Example 5: 
# 
#  
# Input: s = "{[]}"
# Output: true
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 104 
#  s consists of parentheses only '()[]{}'. 
#  
#  Related Topics String Stack 
#  👍 7432 👎 303


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for p in s:
            if p == '(' or p == '[' or p == '{':
                stack.append(p)
            else:
                if len(stack) == 0:
                    return False
                elif p == ')' and stack[-1] != '(':
                    return False
                elif p == ']' and stack[-1] != '[':
                    return False
                elif p == '}' and stack[-1] != '{':
                    return False
                stack.pop()
        if len(stack) == 0:
            return True
        else:
            return False


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    s = Solution()
    a = s.isValid('{[]}')
    print(a)
