#
# @lc app=leetcode id=96 lang=python3
#
# [96] Unique Binary Search Trees
#

# @lc code=start


class Solution:
    def numTrees(self, n: int) -> int:
        # 卡特兰数，Cn+1=Ci*Cn-i
        sumNode = [1, 1]
        if n > 1:
            for i in range(2, n + 1): # i可以视为n-1
                sum = 0
                for j in range(0, i): # 卡特兰数种i范围为0到n，这里n=i+1，j视为i，所以j的范围是[0,i)
                    sum += sumNode[j] * sumNode[i - j - 1]
                sumNode.append(sum)
        return sumNode[n]


# @lc code=end
