#!/usr/bin/env python
# encoding: utf-8
"""
@author: dstch
@license: (C) Copyright 2013-2019, Regulus Tech.
@contact: dstch@163.com
@file: Sort_List.py
@time: 2019/4/1 19:16
@desc: Sort a linked list in O(n log n) time using constant space complexity.
"""
from util import ListNode


class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # insert sort
        temp_head = ListNode(0)
        temp_head.next = head
        cur = head
        pre = temp_head
        while cur is not None:
            tmp = temp_head
            while tmp.next != cur and tmp.next.val < cur.val:
                tmp = tmp.next
            if tmp.next != cur:
                pre.next = cur.next
                cur.next = tmp.next
                tmp.next = cur
            else:
                pre = pre.next
            cur = pre.next
        return temp_head.next


if __name__ == '__main__':
    head = ListNode.build_linked_list([-1, 5, 3, 4, 0])
    s = Solution()
    print(ListNode.show_linked_list(s.sortList(head)))
