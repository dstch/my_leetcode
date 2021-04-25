# You are a professional robber planning to rob houses along a street. Each hous
# e has a certain amount of money stashed, the only constraint stopping you from r
# obbing each of them is that adjacent houses have security systems connected and 
# it will automatically contact the police if two adjacent houses were broken into
#  on the same night. 
# 
#  Given an integer array nums representing the amount of money of each house, r
# eturn the maximum amount of money you can rob tonight without alerting the polic
# e. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 
# (money = 1).
# Total amount you can rob = 2 + 9 + 1 = 12.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 100 
#  0 <= nums[i] <= 400 
#  
#  Related Topics Dynamic Programming 
#  👍 6897 👎 195


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def rob(self, nums: List[int]) -> int:
        res = [-1] * len(nums)

        def func(start):
            if start >= len(nums):
                return 0
            if res[start] != -1:
                return res[start]
            res[start] = max(
                func(start + 1), nums[start] + func(start + 2)
            )
            return res[start]

        func(0)
        return res[0]
# leetcode submit region end(Prohibit modification and deletion)
