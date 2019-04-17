#!/usr/bin/env python
# encoding: utf-8
"""
@author: dstch
@license: (C) Copyright 2013-2019, Regulus Tech.
@contact: dstch@163.com
@file: Odd_Even_Linked_List.py
@time: 2019/4/17 15:24
@desc: Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example 1:

Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL

Example 2:

Input: 2->1->3->5->6->4->7->NULL
Output: 2->3->6->7->1->5->4->NULL
"""

from util import ListNode


class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        temp_head = ListNode(-1)
        temp_head.next = head
        fast = temp_head
        pre = None
        cur = fast
        while cur is not None and cur.next is not None:
            pre = cur.next
            tmp = cur.next.next
            cur.next = None
            cur = tmp
            if cur is None:
                break
            else:
                pre.next = cur.next
                fast.next = cur
                fast = cur
        if pre is not None:
            pre.next = temp_head.next
        return head


if __name__ == '__main__':
    head = ListNode.build_linked_list([2, 1, 3, 5, 6, 4, 7])
    s = Solution()
    print(ListNode.show_linked_list(s.oddEvenList(head)))
