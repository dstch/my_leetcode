# Given a string columnTitle that represents the column title as appear in an Ex
# cel sheet, return its corresponding column number. 
# 
#  For example: 
# 
#  
# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28 
# ...
#  
# 
#  
#  Example 1: 
# 
#  
# Input: columnTitle = "A"
# Output: 1
#  
# 
#  Example 2: 
# 
#  
# Input: columnTitle = "AB"
# Output: 28
#  
# 
#  Example 3: 
# 
#  
# Input: columnTitle = "ZY"
# Output: 701
#  
# 
#  Example 4: 
# 
#  
# Input: columnTitle = "FXSHRXW"
# Output: 2147483647
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= columnTitle.length <= 7 
#  columnTitle consists only of uppercase English letters. 
#  columnTitle is in the range ["A", "FXSHRXW"]. 
#  
#  Related Topics Math 
#  👍 1676 👎 200


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        s = 0
        for word in columnTitle:
            s = s * 26 + ord(word) - 64
        return s


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    res = 0
    a = '10'
    for i in a:
        res = res * 2 + int(i)
    print(res)
