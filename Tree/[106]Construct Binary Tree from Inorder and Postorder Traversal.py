# Given two integer arrays inorder and postorder where inorder is the inorder tr
# aversal of a binary tree and postorder is the postorder traversal of the same tr
# ee, construct and return the binary tree. 
# 
#  
#  Example 1: 
# 
#  
# Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
# Output: [3,9,20,null,null,15,7]
#  
# 
#  Example 2: 
# 
#  
# Input: inorder = [-1], postorder = [-1]
# Output: []
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= inorder.length <= 3000 
#  postorder.length == inorder.length 
#  -3000 <= inorder[i], postorder[i] <= 3000 
#  inorder and postorder consist of unique values. 
#  Each value of postorder also appears in inorder. 
#  inorder is guaranteed to be the inorder traversal of the tree. 
#  postorder is guaranteed to be the postorder traversal of the tree. 
#  
#  Related Topics Array Tree Depth-first Search 
#  👍 2444 👎 45


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def buildTree(self, inorder: list, postorder: list) -> TreeNode:
        if len(postorder) == 0:
            return None
        if len(postorder) == 1:
            return TreeNode(postorder[-1])
        root = TreeNode(postorder[-1])
        index = inorder.index(root.val)
        root.left = self.buildTree(inorder[:index], postorder[:index])
        root.right = self.buildTree(inorder[index + 1:], postorder[index :-1])
        return root
# leetcode submit region end(Prohibit modification and deletion)
