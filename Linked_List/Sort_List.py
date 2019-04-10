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

        def find_mid(head):
            slow = head
            fast = head
            pre = None
            while fast is not None and fast.next is not None:
                pre = slow
                slow = slow.next
                fast = fast.next.next
            pre.next = None
            return slow

        def merge_array(first, last):
            temp_head = ListNode(-1)
            if first.val > last.val:
                temp_head.next = last
            else:
                temp_head.next = first
                first = last
            tmp = temp_head.next
            pre = temp_head
            while first is not None and tmp is not None:
                if tmp.val > first.val:
                    t = first.next
                    pre.next = first
                    first.next = tmp
                    pre = first
                    first = t
                    # tmp = tmp.next
                else:
                    pre = tmp
                    tmp = tmp.next
                    # first = first.next
            if first is not None:
                pre.next = first
            return temp_head.next

        def merge_sort(head):
            if head.next is None:
                return head
            else:
                mid = find_mid(head)
                l = merge_sort(head)
                r = merge_sort(mid)
                return merge_array(l, r)

        if head is None:
            return head
        return merge_sort(head)


if __name__ == '__main__':
    head = ListNode.build_linked_list([4, 2, 1, 3])  # ([-1, 5, 3, 4, 0])
    s = Solution()
    print(ListNode.show_linked_list(s.sortList2(head)))
