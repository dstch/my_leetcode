#!/usr/bin/env python
# encoding: utf-8
"""
@author: dstch
@license: (C) Copyright 2013-2019, Regulus Tech.
@contact: dstch@163.com
@file: Remove_Duplicates_from_Sorted_List.py
@time: 2019/3/3 10:25
@desc: Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2

Example 2:

Input: 1->1->2->3->3
Output: 1->2->3
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        temp_head = ListNode(-1)
        temp_head.next = head
        cur = head
        prev = temp_head
        flag = False
        while cur is not None:
            if cur.next is not None:
                if cur.val == cur.next.val:
                    flag = True
                else:
                    if flag:
                        prev.next = cur
                        flag = False
                    prev = prev.next
            else:
                if flag:
                    prev.next = cur
            cur = cur.next
        return temp_head.next


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(1)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(3)
    head.next.next.next.next = ListNode(3)
    s = Solution()
    result = s.deleteDuplicates(head)
    print(head)
