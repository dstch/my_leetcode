# Write an efficient algorithm that searches for a value in an m x n matrix. Thi
# s matrix has the following properties: 
# 
#  
#  Integers in each row are sorted from left to right. 
#  The first integer of each row is greater than the last integer of the previou
# s row. 
#  
# 
#  
#  Example 1: 
# 
#  
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true
#  
# 
#  Example 2: 
# 
#  
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false
#  
# 
#  
#  Constraints: 
# 
#  
#  m == matrix.length 
#  n == matrix[i].length 
#  1 <= m, n <= 100 
#  -104 <= matrix[i][j], target <= 104 
#  
#  Related Topics Array Binary Search 
#  👍 3234 👎 195


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        l = 0
        r = len(matrix) - 1
        mid = 0
        while l <= r:
            mid = l + (r - l) // 2
            if matrix[mid][0] > target:
                r = mid - 1
            elif matrix[mid][0] < target:
                l = mid + 1
            else:
                return True

        line = l + (r - l) // 2
        l, r = 0, len(matrix[0]) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if matrix[line][mid] > target:
                r = mid - 1
            elif matrix[line][mid] < target:
                l = mid + 1
            else:
                return True
        return False


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    s = Solution()
    a = s.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 11)
    print(a)
