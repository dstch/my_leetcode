#
# @lc app=leetcode id=95 lang=python3
#
# [95] Unique Binary Search Trees II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def generateTreesDFS(left, right):
            res = []
            if left > right:
                return [None]
            for i in range(left, right+1):
                left_nodes = generateTreesDFS(left, i-1)
                right_nodes = generateTreesDFS(i+1, right)
                for left_node in left_nodes:
                    for right_node in right_nodes:
                        root = TreeNode(i)
                        root.left = left_node
                        root.right = right_node
                        res.append(root)
            return res
        if n == 0:
            return []
        else:
            return generateTreesDFS(1, n)

# @lc code=end
