#!/usr/bin/env python
# encoding: utf-8
"""
@author: dstch
@license: (C) Copyright 2013-2019, Regulus Tech.
@contact: dstch@163.com
@file: Remove_Duplicates_from_Sorted_List_II.py
@time: 2019/3/2 8:13
@desc: Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

Example 1:

Input: 1->2->3->3->4->4->5
Output: 1->2->5

Example 2:

Input: 1->1->1->2->3
Output: 2->3
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
                        prev.next = cur.next
                        flag = False
                    else:
                        prev = prev.next
            else:
                if flag:
                    prev.next = cur.next
            cur = cur.next
        return temp_head.next


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(1)
    head.next.next = ListNode(3)
    s = Solution()
    result = s.deleteDuplicates(head)
    print(result)
