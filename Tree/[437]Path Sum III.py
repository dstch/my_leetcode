# You are given a binary tree in which each node contains an integer value. 
# 
#  Find the number of paths that sum to a given value. 
# 
#  The path does not need to start or end at the root or a leaf, but it must go 
# downwards
# (traveling only from parent nodes to child nodes). 
# 
#  The tree has no more than 1,000 nodes and the values are in the range -1,000,
# 000 to 1,000,000.
# 
#  Example:
#  
# root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8
# 
#       10
#      /  \
#     5   -3
#    / \    \
#   3   2   11
#  / \   \
# 3  -2   1
# 
# Return 3. The paths that sum to 8 are:
# 
# 1.  5 -> 3
# 2.  5 -> 2 -> 1
# 3. -3 -> 11
#  
#  Related Topics Tree 
#  👍 4857 👎 319


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        li = []
        curSum = 0
        res = 0

        def func(node, li, curSum, sum, res):
            if node is None:
                return res
            li.append(node.val)
            curSum += node.val
            if curSum == sum:
                res += 1
            temp = curSum
            for val in li[:-1]:
                temp -= val
                if temp == sum:
                    res += 1
            res += func(node.left, li, curSum, sum, 0)
            res += func(node.right, li, curSum, sum, 0)
            li.pop()
            return res

        res = func(root, li, curSum, sum, res)
        return res

# leetcode submit region end(Prohibit modification and deletion)
