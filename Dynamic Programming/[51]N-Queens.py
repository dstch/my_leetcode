# The n-queens puzzle is the problem of placing n queens on an n x n chessboard 
# such that no two queens attack each other. 
# 
#  Given an integer n, return all distinct solutions to the n-queens puzzle. 
# 
#  Each solution contains a distinct board configuration of the n-queens' placem
# ent, where 'Q' and '.' both indicate a queen and an empty space, respectively. 
# 
#  
#  Example 1: 
# 
#  
# Input: n = 4
# Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as show
# n above
#  
# 
#  Example 2: 
# 
#  
# Input: n = 1
# Output: [["Q"]]
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= n <= 9 
#  
#  Related Topics Backtracking 
#  👍 2875 👎 107


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def solveNQueens(self, n: int):  # -> List[List[str]]:
        import copy
        res = []
        queens_str = '.' * n
        queens = [queens_str] * n  # 选择列表

        def isValid(queens_list, row, col):
            m = len(queens_list) - 1
            for i in range(m):
                if queens_list[i][col] == 'Q':
                    return False  # 检查同一列是否有Q

            for (i, j) in zip(range(row, -1, -1), range(col, -1, -1)):
                if queens_list[i][j] == 'Q':
                    return False  # 检查左上方是否有Q

            for (i, j) in zip(range(row, -1, -1), range(col, n)):
                if queens_list[i][j] == 'Q':
                    return False  # 检查右上方是否有Q

            return True

        def func(queens_list, row):
            if row == len(queens_list):
                res.append(copy.deepcopy(queens_list))
                return
            for col in range(n):
                if isValid(queens_list, row, col):
                    queens_list[row] = queens_list[row][:col] + 'Q' + queens_list[row][col + 1:]
                    func(queens_list, row + 1)  # 每次递归row+1，所以相同row不会有多个Q
                    queens_list[row] = queens_list[row][:col] + '.' + queens_list[row][col + 1:]
                else:
                    continue

        func(queens, 0)
        return res


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    s = Solution()
    s.solveNQueens(4)
