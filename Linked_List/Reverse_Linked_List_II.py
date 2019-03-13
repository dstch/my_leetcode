#!/usr/bin/env python
# encoding: utf-8
"""
@author: dstch
@license: (C) Copyright 2013-2019, Regulus Tech.
@contact: dstch@163.com
@file: Reverse_Linked_List_II.py
@time: 2019/3/5 11:51
@desc: Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
"""
from util import ListNode


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        # add dummy node
        temp_head = ListNode(-1)
        temp_head.next = head
        prev = temp_head
        cur = head
        count = 1
        while cur is not None:
            if count < m:
                cur = cur.next
                prev = prev.next
            elif count == m:
                first_prev = prev
                first = cur
                cur = cur.next
                prev = prev.next
            elif count > m and count <= n:
                prev.next = cur.next
                cur.next = first
                first_prev.next = cur

                first = cur
                cur = prev.next
            else:
                break
            count += 1
        return temp_head.next


if __name__ == '__main__':
    head = ListNode.build_linked_list([1, 2, 3, 4, 5])
    s = Solution()
    result = s.reverseBetween(head, 2, 4)
    print(ListNode.show_linked_list(result))
