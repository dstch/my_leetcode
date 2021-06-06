# Suppose an array of length n sorted in ascending order is rotated between 1 an
# d n times. For example, the array nums = [0,1,2,4,5,6,7] might become: 
# 
#  
#  [4,5,6,7,0,1,2] if it was rotated 4 times. 
#  [0,1,2,4,5,6,7] if it was rotated 7 times. 
#  
# 
#  Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results 
# in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]]. 
# 
#  Given the sorted rotated array nums of unique elements, return the minimum el
# ement of this array. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [3,4,5,1,2]
# Output: 1
# Explanation: The original array was [1,2,3,4,5] rotated 3 times.
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [4,5,6,7,0,1,2]
# Output: 0
# Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times
# .
#  
# 
#  Example 3: 
# 
#  
# Input: nums = [11,13,15,17]
# Output: 11
# Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 
# 
#  
# 
#  
#  Constraints: 
# 
#  
#  n == nums.length 
#  1 <= n <= 5000 
#  -5000 <= nums[i] <= 5000 
#  All the integers of nums are unique. 
#  nums is sorted and rotated between 1 and n times. 
#  
#  Related Topics Array Binary Search 
#  👍 3447 👎 305


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        这个问题主要分成如下三种情况
        l<mid>r
        l>mid<r
        l<mid<r
        如果发生旋转的话，那么nums[r]<nums[l]一定成立（非常容易证明），所以对于第一种情况最小值一定在右侧，
        所以我们更新low=mid+1，对于第二种情况最小值一定在左侧或者就在mid，这要怎么理解呢？如果最小值在右侧的话，
        说明nums[mid]比最小值大，那么nums[mid]一定是大于nums[low]的（与题目条件不符），所以原结论成立，
        所以我们更新high=mid。对于第三种情况，最小值一定是nums[low]。
        但是上述结论仅适用于len(nums)>=3的情况，对于len(nums)<3的情况，我们要加以修正。
        l<=mid>r
        l>mid<=r
        l<=mid<=r
        :param nums:
        :return:
        """
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] >= nums[l] and nums[mid] > nums[r]:
                l = mid + 1
            elif nums[mid] < nums[l] and nums[mid] <= nums[r]:
                r = mid
            elif nums[l] <= nums[mid] <= nums[r]:
                return nums[l]
        return -1

# leetcode submit region end(Prohibit modification and deletion)
