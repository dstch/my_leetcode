#!/usr/bin/env python
# encoding: utf-8
"""
@author: dstch
@license: (C) Copyright 2013-2019, Regulus Tech.
@contact: dstch@163.com
@file: Insertion_Sort_List.py
@time: 2019/3/28 8:53
@desc: Sort a linked list using insertion sort.
"""
from util import ListNode


class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        temp_head = ListNode(-1)
        temp_head.next = head
        cur = head
        pre = temp_head
        while cur is not None:
            tmp = cur.next
            # find insert position
            while tmp is not None and tmp.val <= cur.val:
                tmp = tmp.next
            if tmp is not None and tmp != cur.next:
                pre.next = cur.next
                cur.next = tmp.next
                tmp.next = cur
            else:
                pre = pre.next
            cur = pre.next
        return temp_head.next


if __name__ == '__main__':
    head = ListNode.build_linked_list([4, 2, 1, 3])
    s = Solution()
    print(ListNode.show_linked_list(s.insertionSortList(head)))
