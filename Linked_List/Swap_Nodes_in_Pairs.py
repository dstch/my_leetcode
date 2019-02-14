#!/usr/bin/env python
# encoding: utf-8
"""
@author: dstch
@license: (C) Copyright 2013-2019, Regulus Tech.
@contact: dstch@163.com
@file: Swap_Nodes_in_Pairs.py
@time: 2019/1/15 22:10
@desc: Given a linked list, swap every two adjacent nodes and return its head.

Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head != None:
            if head.next != None:
                return_head = head.next
                left = head
                right = head.next
                while left != None:
                    right = left.next
                    left.next = right.next
                    right.next = left
                    left = left.next
                    # right = left.next
            else:
                return_head = head
        else:
            return head
        return return_head


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    s = Solution()
    s.swapPairs(head)
    # output: [2,1,3]
