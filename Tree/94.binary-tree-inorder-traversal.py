#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        def func(node, result_list):
            if node is not None:
                func(node.left, result_list)
                result_list.append(node.val)
                func(node.right, result_list)
        result = []
        func(root, result)
        return result

# @lc code=end
