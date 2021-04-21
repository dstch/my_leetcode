# Given two sorted arrays nums1 and nums2 of size m and n respectively, return t
# he median of the two sorted arrays. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
#  
# 
#  Example 2: 
# 
#  
# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
#  
# 
#  Example 3: 
# 
#  
# Input: nums1 = [0,0], nums2 = [0,0]
# Output: 0.00000
#  
# 
#  Example 4: 
# 
#  
# Input: nums1 = [], nums2 = [1]
# Output: 1.00000
#  
# 
#  Example 5: 
# 
#  
# Input: nums1 = [2], nums2 = []
# Output: 2.00000
#  
# 
#  
#  Constraints: 
# 
#  
#  nums1.length == m 
#  nums2.length == n 
#  0 <= m <= 1000 
#  0 <= n <= 1000 
#  1 <= m + n <= 2000 
#  -106 <= nums1[i], nums2[i] <= 106 
#  
# 
#  
# Follow up: The overall run time complexity should be O(log (m+n)). Related Top
# ics Array Binary Search Divide and Conquer 
#  👍 9773 👎 1498


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        https://blog.csdn.net/wangzibai/article/details/102982088
        https://blog.csdn.net/guotianqing/article/details/87527614

        把两个数组一起分成两部分，需要满足 i+j=m-i+n-j+1和B[j-1] <= A[i] 并且 A[i-1] <= B[j]，这里注意：

        i+j = m-i+n-j;
        i+j = m-i+n-j+1;//加一是因为如果两个数组总数为奇数那么左半部分就比右半部分多一个数字
        综上得j=(m+n+1)/2-i;// 因为+1之后/2有因为转为int之后会屏蔽0.5所以这个+1并没有影响但是却可以统合奇偶不同的问题

        达到条件后，中位数mid=(max(left_part) + min(right_part))/2
        :param nums1:
        :param nums2:
        :return:
        """
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        m, n = len(nums1), len(nums2)  # m<n
        imin, imax = 0, m
        while imin <= imax:
            i = (imin + imax) // 2
            j = (m + n + 1) // 2 - i  # i,j有约束条件
            if i > 0 and nums1[i - 1] > nums2[j]:  # 第二个条件，即左半部分需要小于右半部分，因为两个数组有序，所以只讨论边界
                imin -= 1
            elif i < m and nums1[i] < nums2[j - 1]:
                imax += 1
            else:
                if i == 0:  # nums1长度为0，可以认为左边最大为nums2的第j-1个
                    max_of_left = nums2[j - 1]
                elif j == 0:
                    max_of_left = nums1[i - 1]
                else:
                    max_of_left = max(nums1[i - 1], nums2[j - 1])

                if (m + n) % 2 == 1:  # 数组长度一共是奇数，可以直接返回中位数
                    return max_of_left

                if i == m:
                    min_of_right = nums2[j]
                elif j == n:
                    min_of_right = nums1[i]
                else:
                    min_of_right = min(nums1[i], nums2[j])

                return (min_of_right + max_of_left) / 2

# leetcode submit region end(Prohibit modification and deletion)
