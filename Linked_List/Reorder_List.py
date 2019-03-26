#!/usr/bin/env python
# encoding: utf-8
"""
@author: dstch
@license: (C) Copyright 2013-2019, Regulus Tech.
@contact: dstch@163.com
@file: Reorder_List.py
@time: 2019/3/25 18:40
@desc: Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.

Example 2:

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
"""
from util import ListNode


class Solution(object):
    def reorderList(self, head: ListNode):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if head is None:
            return head
        # split list
        middle_head = self.splitList(head)
        tmp = middle_head.next
        middle_head.next = None
        middle_head = tmp
        # reverse list
        reverse_head = self.reverseList(middle_head)
        return_head = head
        cur = head
        reverse_cur = reverse_head
        while cur is not None and reverse_cur is not None:
            if cur != reverse_cur:
                tmp = cur.next
                cur.next = reverse_cur
                reverse_cur = tmp
                cur = cur.next
            else:
                cur.next = None
                break
        return return_head

    def splitList(self, head):
        fast = head
        slow = head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow

    def reverseList(self, head):
        cur = head
        prev = None
        while cur is not None:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        return prev

    def reverseList2(self, head):
        cur = head
        c = ListNode(head.val)
        prev = None
        while cur is not None:
            tmp = cur.next
            c.next = prev
            prev = c
            if tmp is None:
                break
            c = ListNode(tmp.val)
            cur = tmp
        return prev


if __name__ == '__main__':
    head = ListNode.build_linked_list([1, 2, 3, 4])
    s = Solution()
    s.reorderList(head)
