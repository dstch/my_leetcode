# Given an array nums of n integers, return an array of all the unique quadruple
# ts [nums[a], nums[b], nums[c], nums[d]] such that: 
# 
#  
#  0 <= a, b, c, d < n 
#  a, b, c, and d are distinct. 
#  nums[a] + nums[b] + nums[c] + nums[d] == target 
#  
# 
#  You may return the answer in any order. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [2,2,2,2,2], target = 8
# Output: [[2,2,2,2]]
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 200 
#  -109 <= nums[i] <= 109 
#  -109 <= target <= 109 
#  
#  Related Topics Array Hash Table Two Pointers 
#  👍 3174 👎 406


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        for i, a in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1] or i + 1 == len(nums):
                continue
            for j in range(i + 1, len(nums)):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                left = j + 1
                right = len(nums) - 1
                while left < right:
                    s = a + nums[j] + nums[left] + nums[right]
                    if s == target:
                        print(i, j, left, right)
                        res.append([a, nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                    elif s > target:
                        right -= 1
                    else:
                        left += 1
        return res
# leetcode submit region end(Prohibit modification and deletion)
