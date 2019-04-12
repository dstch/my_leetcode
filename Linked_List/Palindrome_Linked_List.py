#!/usr/bin/env python
# encoding: utf-8
"""
@author: dstch
@license: (C) Copyright 2013-2019, Regulus Tech.
@contact: dstch@163.com
@file: Palindrome_Linked_List.py
@time: 2019/4/12 11:46
@desc: Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false

Example 2:

Input: 1->2->2->1
Output: true
"""

from util import ListNode


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return True
        slow = head
        fast = head
        pre = None
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            tmp = slow.next
            slow.next = pre
            pre = slow
            slow = tmp
        first = pre
        last = slow
        if first.val != last.val:
            last = last.next
        while first is not None and last is not None and first.val == last.val:
            first = first.next
            last = last.next
        if first is None and last is None:
            return True
        else:
            return False


if __name__ == '__main__':
    head = ListNode.build_linked_list([1, 0, 1])  # ([-1, 5, 3, 4, 0])
    s = Solution()
    print(s.isPalindrome(head))
