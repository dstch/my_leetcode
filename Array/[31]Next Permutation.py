# Implement next permutation, which rearranges numbers into the lexicographicall
# y next greater permutation of numbers. 
# 
#  If such an arrangement is not possible, it must rearrange it as the lowest po
# ssible order (i.e., sorted in ascending order). 
# 
#  The replacement must be in place and use only constant extra memory. 
# 
#  
#  Example 1: 
#  Input: nums = [1,2,3]
# Output: [1,3,2]
#  Example 2: 
#  Input: nums = [3,2,1]
# Output: [1,2,3]
#  Example 3: 
#  Input: nums = [1,1,5]
# Output: [1,5,1]
#  Example 4: 
#  Input: nums = [1]
# Output: [1]
#  
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 100 
#  0 <= nums[i] <= 100 
#  
#  Related Topics Array 
#  👍 5315 👎 1828


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def nextPermutation(self, nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # pre_index = len(nums) - 2
        # after_index = len(nums) - 1
        # while pre_index >= 0 and nums[pre_index] >= nums[pre_index + 1]:
        #     pre_index -= 1
        # if pre_index >= 0:
        #     while nums[after_index] <= nums[pre_index]:
        #         after_index -= 1
        #     nums[pre_index], nums[after_index] = nums[after_index], nums[pre_index]
        # nums[pre_index + 1:] = sorted(nums[pre_index + 1:])

        i = len(nums) - 2
        j = i + 1
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i >= 0:
            while nums[i] >= nums[j]:
                j -= 1
            nums[j], nums[i] = nums[i], nums[j]
        nums[i + 1:] = nums[i + 1:][::-1]


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    nums = [2, 3, 1] #[312]
    # nums = [1, 2, 3]
    s = Solution()
    s.nextPermutation(nums)
    print(nums)
