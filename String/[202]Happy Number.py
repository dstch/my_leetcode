# Write an algorithm to determine if a number n is happy. 
# 
#  A happy number is a number defined by the following process: 
# 
#  
#  Starting with any positive integer, replace the number by the sum of the squa
# res of its digits. 
#  Repeat the process until the number equals 1 (where it will stay), or it loop
# s endlessly in a cycle which does not include 1. 
#  Those numbers for which this process ends in 1 are happy. 
#  
# 
#  Return true if n is a happy number, and false if not. 
# 
#  
#  Example 1: 
# 
#  
# Input: n = 19
# Output: true
# Explanation:
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1
#  
# 
#  Example 2: 
# 
#  
# Input: n = 2
# Output: false
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= n <= 231 - 1 
#  
#  Related Topics Hash Table Math 
#  👍 3163 👎 518


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isHappy(self, n: int) -> bool:
        num = str(n)
        temp = []
        while num not in temp:
            res = 0
            temp.append(num)
            for i in num:
                res += pow(int(i), 2)
            num = str(res)
        if num == '1':
            return True
        return False


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    s = Solution()
    s.isHappy(19)
