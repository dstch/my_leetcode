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
        if m == n:
            return head
        count = 1
        first = head
        prev = None
        cur = head
        while cur is not None:
            if count < m:
                first = cur
                cur = cur.next
            elif count >= m and count <= n:
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp
            else:
                first.next = prev
                while prev.next is not None:
                    prev = prev.next
                prev.next = cur
                break
            count += 1
        return first


if __name__ == '__main__':
    head = ListNode.build_linked_list([3, 5])
    s = Solution()
    result = s.reverseBetween(head, 1, 1)
    print(result)
