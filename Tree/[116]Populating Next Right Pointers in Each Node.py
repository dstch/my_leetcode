# You are given a perfect binary tree where all leaves are on the same level, an
# d every parent has two children. The binary tree has the following definition: 
# 
#  
# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }
#  
# 
#  Populate each next pointer to point to its next right node. If there is no ne
# xt right node, the next pointer should be set to NULL. 
# 
#  Initially, all next pointers are set to NULL. 
# 
#  
# 
#  Follow up: 
# 
#  
#  You may only use constant extra space. 
#  Recursive approach is fine, you may assume implicit stack space does not coun
# t as extra space for this problem. 
#  
# 
#  
#  Example 1: 
# 
#  
# 
#  
# Input: root = [1,2,3,4,5,6,7]
# Output: [1,#,2,3,#,4,5,6,7,#]
# Explanation: Given the above perfect binary tree (Figure A), your function sho
# uld populate each next pointer to point to its next right node, just like in Fig
# ure B. The serialized output is in level order as connected by the next pointers
# , with '#' signifying the end of each level.
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the given tree is less than 4096. 
#  -1000 <= node.val <= 1000 
#  Related Topics Tree Depth-first Search Breadth-first Search 
#  👍 3093 👎 161


# leetcode submit region begin(Prohibit modification and deletion)
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        def func(node1, node2):
            if node1 is not None and node2 is not None:
                node1.next = node2
                func(node1.left, node1.right)
                func(node1.right, node2.left)
                func(node2.left, node2.right)

        if root is None:
            return None
        func(root.left, root.right)
        return root

# leetcode submit region end(Prohibit modification and deletion)
