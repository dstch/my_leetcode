# Given an array of integers nums sorted in ascending order, find the starting a
# nd ending position of a given target value. 
# 
#  If target is not found in the array, return [-1, -1]. 
# 
#  Follow up: Could you write an algorithm with O(log n) runtime complexity? 
# 
#  
#  Example 1: 
#  Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
#  Example 2: 
#  Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
#  Example 3: 
#  Input: nums = [], target = 0
# Output: [-1,-1]
#  
#  
#  Constraints: 
# 
#  
#  0 <= nums.length <= 105 
#  -109 <= nums[i] <= 109 
#  nums is a non-decreasing array. 
#  -109 <= target <= 109 
#  
#  Related Topics Array Binary Search 
#  👍 5306 👎 205


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        flag = False
        mid = 0
        while left <= right:
            mid = left + int((right - left) / 2)
            if nums[mid] == target:
                flag = True
                break
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        if flag:
            left, right = mid, mid
            while left > 0 and nums[left - 1] == target:
                left -= 1
            while right < len(nums) - 1 and nums[right + 1] == target:
                right += 1
            return [left, right]
        return [-1, -1]
# leetcode submit region end(Prohibit modification and deletion)
