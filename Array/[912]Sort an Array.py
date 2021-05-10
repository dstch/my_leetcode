# Given an array of integers nums, sort the array in ascending order. 
# 
#  
#  Example 1: 
#  Input: nums = [5,2,3,1]
# Output: [1,2,3,5]
#  Example 2: 
#  Input: nums = [5,1,1,2,0,0]
# Output: [0,0,1,1,2,5]
#  
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 5 * 104 
#  -5 * 104 <= nums[i] <= 5 * 104 
#  
#  👍 853 👎 373


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # def quick_sort(s, l, r):
        #     if l < r:
        #         i, j = l, r
        #         x = s[i]
        #         while i < j:
        #             while i < j and s[j] >= x:
        #                 j -= 1
        #             if i < j:
        #                 s[i] = s[j]
        #                 i += 1
        #             while i < j and s[i] <= x:
        #                 i += 1
        #             if i < j:
        #                 s[j] = s[i]
        #                 j -= 1
        #         s[i] = x
        #         quick_sort(s, l, i - 1)
        #         quick_sort(s, i + 1, r)
        #
        # quick_sort(nums, 0, len(nums) - 1)
        # return nums
        if len(nums) == 1:
            return nums
        if not nums:
            return []
        pick = random.choice(nums)
        left, mid, right = [], [], []
        for i in nums:
            if i < pick:
                left.append(i)
            elif i > pick:
                right.append(i)
            else:
                mid.append(i)
        return self.sortArray(left) + mid + self.sortArray(right)
        # def quicksort3(s, left, right):
        #     if right - left < 1:
        #         return
        #     pivot = s[left]
        #     lo, hi = left, right
        #     while lo < hi:
        #         while lo < hi and s[hi] >= pivot:
        #             hi -= 1
        #         while lo < hi and s[lo] <= pivot:
        #             lo += 1
        #         if lo < hi:
        #             s[lo], s[hi] = s[hi], s[lo]
        #     s[left], s[lo] = s[lo], pivot
        #     quicksort3(s, left, lo - 1)
        #     quicksort3(s, lo + 1, right)
        #
        # quicksort3(nums, 0, len(nums) - 1)
        # return nums

# leetcode submit region end(Prohibit modification and deletion)
