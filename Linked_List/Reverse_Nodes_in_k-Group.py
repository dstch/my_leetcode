#!/usr/bin/env python
# encoding: utf-8
"""
@author: dstch
@license: (C) Copyright 2013-2019, Regulus Tech.
@contact: dstch@163.com
@file: Reverse_Nodes_in_k-Group.py
@time: 2019/2/16 21:09
@desc: Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not
a multiple of k then left-out nodes in the end should remain as it is.

Example:

Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseKGroup(self, head: 'ListNode', k: 'int') -> 'ListNode':
        # add dummy node
        tmp_head = ListNode(0)
        tmp_head.next = head
        pre_head = tmp_head
        cur = head
        while cur is not None:
            next = cur
            for i in range(k):
                if next is None:
                    break
                next = next.next
            prev, cur = self.reverseList(cur, next)
            cur.next = next
            tmp_head.next = prev
            tmp_head = cur
            cur = prev
            for i in range(k):
                if cur is None:
                    break
                cur = cur.next
        return pre_head.next

    def reverseList(self, sub_head: 'ListNode', last: 'ListNode') -> '[ListNode]':
        cur = sub_head
        prev = None
        while cur != last:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        return prev, sub_head


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    s = Solution()
    result = s.reverseKGroup(head, 2)
    print(result)
