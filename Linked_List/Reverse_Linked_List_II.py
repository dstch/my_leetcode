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
        temp_head = ListNode(-1)
        temp_head.next = head
        cur = head
        prev = temp_head
        cur_1 = head
        prev_1 = temp_head
        cur_2 = cur_1
        prev_2 = prev_1
        for i in range(n):
            if i + 1 == m:
                cur_1 = cur
                prev_1 = prev
            elif i + 1 == n:
                cur_2 = cur
                prev_2 = prev
            cur = cur.next
            prev = prev.next
        prev_2.next = cur_1
        next = cur_1.next
        cur_1.next = cur_2.next
        prev_1.next = cur_2
        cur_2.next = next
        return temp_head.next


if __name__ == '__main__':
    head = ListNode.build_linked_list([1, 2, 3, 4])
    s = Solution()
    result = s.reverseBetween(head, 1, 4)
    print(result)
