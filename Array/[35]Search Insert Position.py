# Given a sorted array of distinct integers and a target value, return the index
#  if the target is found. If not, return the index where it would be if it were i
# nserted in order. 
# 
#  
#  Example 1: 
#  Input: nums = [1,3,5,6], target = 5
# Output: 2
#  Example 2: 
#  Input: nums = [1,3,5,6], target = 2
# Output: 1
#  Example 3: 
#  Input: nums = [1,3,5,6], target = 7
# Output: 4
#  Example 4: 
#  Input: nums = [1,3,5,6], target = 0
# Output: 0
#  Example 5: 
#  Input: nums = [1], target = 0
# Output: 0
#  
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 104 
#  -104 <= nums[i] <= 104 
#  nums contains distinct values sorted in ascending order. 
#  -104 <= target <= 104 
#  
#  Related Topics Array Binary Search 
#  👍 3412 👎 287


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + int((right - left) / 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return left
# leetcode submit region end(Prohibit modification and deletion)
