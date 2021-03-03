# Given the root of a binary tree, imagine yourself standing on the right side o
# f it, return the values of the nodes you can see ordered from top to bottom. 
# 
#  
#  Example 1: 
# 
#  
# Input: root = [1,2,3,null,5,null,4]
# Output: [1,3,4]
#  
# 
#  Example 2: 
# 
#  
# Input: root = [1,null,3]
# Output: [1,3]
#  
# 
#  Example 3: 
# 
#  
# Input: root = []
# Output: []
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is in the range [0, 100]. 
#  -100 <= Node.val <= 100 
#  
#  Related Topics Tree Depth-first Search Breadth-first Search Recursion Queue 
#  👍 3559 👎 189


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        res = []

        def func(node, level):
            if len(res) == level:
                res.append([])
            if node is not None:
                res[level].append(node.val)
            if node.left is not None:
                func(node.left, level + 1)
            if node.right is not None:
                func(node.right, level + 1)

        if root is None:
            return []
        func(root, 0)
        return [x[-1] for x in res]

# leetcode submit region end(Prohibit modification and deletion)
