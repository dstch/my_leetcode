#!/usr/bin/env python
# encoding: utf-8
"""
@author: dstch
@license: (C) Copyright 2013-2019, Regulus Tech.
@contact: dstch@163.com
@file: Valid Anagram.py
@time: 2019/9/1 20:53
@desc: Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true

Example 2:

Input: s = "rat", t = "car"
Output: false

"""


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        k1 = {}
        k2 = {}
        for index, n in enumerate(s):
            if n not in k1:
                k1[n] = 1
            else:
                k1[n] += 1
            if t[index] not in k2:
                k2[t[index]] = 1
            else:
                k2[t[index]] += 1
        for k in k1:
            if k in k2 and k1[k] == k2[k]:
                continue
            else:
                return False

        return True
