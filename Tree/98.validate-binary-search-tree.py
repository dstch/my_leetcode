#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def func(root_node, flag):
            if root_node is None or not flag:
                return flag
            if root_node.left is not None:
                flag = flag and func(root_node.left, flag)
            else:
                if root_node.right is None:
                    return flag and True
                else:
                    return flag and root_node.right.val > root_node.val
            if root_node.right is not None:
                flag = flag and func(root_node.right, flag)
            else:
                if root_node.left is None:
                    return flag and True
                else:
                    return flag and root_node.left.val < root_node.val
            if root_node.left.val < root_node.val < root_node.right.val:
                return flag and True
            else:
                return flag and False

        return func(root, True)

# @lc code=end
