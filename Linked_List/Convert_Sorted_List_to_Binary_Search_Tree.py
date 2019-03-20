#!/usr/bin/env python
# encoding: utf-8
"""
@author: dstch
@license: (C) Copyright 2013-2019, Regulus Tech.
@contact: dstch@163.com
@file: Convert_Sorted_List_to_Binary_Search_Tree.py
@time: 2019/3/13 20:09
@desc: Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted linked list: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5

"""
from util import ListNode


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if head is None:
            return None
        if head.next is None:
            return TreeNode(head.val)
        # find middle node by fast & slow point
        fast = head
        slow = head
        last = head
        while fast.next is not None and fast.next.next is not None:
            last = slow
            fast = fast.next.next
            slow = slow.next

        fast = slow.next
        last.next = None
        cur = TreeNode(slow.val)
        if head != slow:
            cur.left = self.sortedListToBST(head)
        cur.right = self.sortedListToBST(fast)
        return cur


if __name__ == '__main__':
    head = ListNode.build_linked_list([-10, -3, 0, 5, 9])
    s = Solution()
    print(s.sortedListToBST(head))
