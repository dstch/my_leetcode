# Given a collection of candidate numbers (candidates) and a target number (targ
# et), find all unique combinations in candidates where the candidate numbers sum 
# to target. 
# 
#  Each number in candidates may only be used once in the combination. 
# 
#  Note: The solution set must not contain duplicate combinations. 
# 
#  
#  Example 1: 
# 
#  
# Input: candidates = [10,1,2,7,6,1,5], target = 8
# Output: 
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]
#  
# 
#  Example 2: 
# 
#  
# Input: candidates = [2,5,2,1,2], target = 5
# Output: 
# [
# [1,2,2],
# [5]
# ]
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= candidates.length <= 100 
#  1 <= candidates[i] <= 50 
#  1 <= target <= 30 
#  
#  Related Topics Array Backtracking 
#  👍 2666 👎 87


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def combinationSum2(self, candidates, target: int):
        import copy
        res = []
        candidates = sorted(candidates)

        def func(temp_res, val, start):
            if val < 0:
                return
            if val == 0:
                res.append(copy.deepcopy(temp_res))
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    # 这个判断的作用是去除结果中的重复
                    # 在这个循环中，每次循环是一个结果数组，结果数组中的元素是在递归中添加，所以这里并不会影响结果数组中的重复数字
                    # 对于这个循环，相邻两个数相同代表两个结果数组是相同的开始，肯定会得到相同的结果，所以跳过
                    continue
                temp_res.append(candidates[i])
                func(temp_res, val - candidates[i], i + 1)
                temp_res.pop()

        func([], target, 0)
        return res


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    a = [1, 6, 6]
    t = 13
    s = Solution()
    res = s.combinationSum2(a, t)
    print(res)
