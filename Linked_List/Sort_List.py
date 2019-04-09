#!/usr/bin/env python
# encoding: utf-8
"""
@author: dstch
@license: (C) Copyright 2013-2019, Regulus Tech.
@contact: dstch@163.com
@file: Sort_List.py
@time: 2019/4/1 19:16
@desc: Sort a linked list in O(n log n) time using constant space complexity.
https://www.cnblogs.com/TenosDoIt/p/3666585.html
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

    def sortList2(self, head):
        """
        merge sort
        :return:
        """

        def find_mid(head, end):
            slow = head
            fast = head
            while fast.next is not None and fast.next != end:
                slow = slow.next
                fast = fast.next.next
            return slow

        def merge_array(first, last):
            temp_head = ListNode(-1)
            if first.val > last.val:
                temp_head.next = last
            else:
                temp_head.next = first
                first = last
            tmp = temp_head.next
            while first is not None and tmp is not None:
                if tmp.val > first.val:
                    t = first.next
                    first.next = tmp.next
                    tmp.next = first
                    tmp = tmp.next.next
                    first = t
                else:
                    tmp = tmp.next
            if first is not None:
                tmp.next = first
            return temp_head.next

        def merge_sort(head, end):
            if head != end:
                mid = find_mid(head, end)
                merge_sort(head, mid)
                merge_sort(mid.next, end)
                merge_array(head, end)
            return head

        return merge_sort(head, None)


if __name__ == '__main__':
    head = ListNode.build_linked_list([-1, 5, 3, 4, 0])
    s = Solution()
    print(ListNode.show_linked_list(s.sortList2(head)))
