# Given an array nums of n integers and an integer target, find three integers i
# n nums such that the sum is closest to target. Return the sum of the three integ
# ers. You may assume that each input would have exactly one solution. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
#  
# 
#  
#  Constraints: 
# 
#  
#  3 <= nums.length <= 10^3 
#  -10^3 <= nums[i] <= 10^3 
#  -10^4 <= target <= 10^4 
#  
#  Related Topics Array Two Pointers 
#  👍 3100 👎 169


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = 0
        gap = 10000
        for index, value in enumerate(nums):
            if index > 0 and nums[index] == nums[index - 1]:
                continue
            left = index + 1
            right = len(nums) - 1
            while left < right:
                v = nums[left] + nums[right] + value
                s = abs(v - target)
                if s < gap:
                    gap = s
                    res = v
                if v > target:
                    right -= 1
                else:
                    left += 1
        return res
        # leetcode submit region end(Prohibit modification and deletion)
