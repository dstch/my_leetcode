# Given a string s which represents an expression, evaluate this expression and 
# return its value. 
# 
#  The integer division should truncate toward zero. 
# 
#  
#  Example 1: 
#  Input: s = "3+2*2"
# Output: 7
#  Example 2: 
#  Input: s = " 3/2 "
# Output: 1
#  Example 3: 
#  Input: s = " 3+5 / 2 "
# Output: 5
#  
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 3 * 105 
#  s consists of integers and operators ('+', '-', '*', '/') separated by some n
# umber of spaces. 
#  s represents a valid expression. 
#  All the integers in the expression are non-negative integers in the range [0,
#  231 - 1]. 
#  The answer is guaranteed to fit in a 32-bit integer. 
#  
#  Related Topics String Stack 
#  👍 2356 👎 361


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def calculate(self, s: str) -> int:
        ss = ['+', '-', '*', '/']
        res = 0
        curRes = 0  # 存储临时计算结果
        num = 0  # 存储数字
        n = len(s)
        op = '+'  # 初始化运算
        for i in range(n):
            char = s[i]
            if char >= '0' and char <= '9':
                num = num * 10 + int(char)
            if char in ss or i == n - 1:
                curRes = int(eval(f'curRes{op}num'))
                if char == '+' or char == '-' or i == n - 1:
                    res += curRes
                    curRes = 0
                op = char
                num = 0
        return res


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    s = Solution()
    s.calculate(" 3+5 / 2 ")
