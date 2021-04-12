# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k
# ]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0. 
# 
#  Notice that the solution set must not contain duplicate triplets. 
# 
#  
#  Example 1: 
#  Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
#  Example 2: 
#  Input: nums = []
# Output: []
#  Example 3: 
#  Input: nums = [0]
# Output: []
#  
#  
#  Constraints: 
# 
#  
#  0 <= nums.length <= 3000 
#  -105 <= nums[i] <= 105 
#  
#  Related Topics Array Two Pointers 
#  👍 10098 👎 1037


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for index, target in enumerate(nums):
            if index != 0 and nums[index] == nums[index - 1]:
                continue  # 去除重复项，因为在index的时候就找过，所以一旦在后续就不需要再找了
            left = index + 1
            right = len(nums) - 1
            while left < right:
                value = nums[left] + nums[right]
                if value + target == 0:
                    res.append([nums[left], nums[right], target])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:  # 去除重复项，如上述去除重复项一样的意思，只不过位置不同
                        left += 1
                elif value + target > 0:
                    right -= 1
                else:
                    left += 1
        return res
    # leetcode submit region end(Prohibit modification and deletion)
