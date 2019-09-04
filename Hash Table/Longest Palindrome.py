#!/usr/bin/env python
# encoding: utf-8
"""
@author: dstch
@license: (C) Copyright 2013-2019, Regulus Tech.
@contact: dstch@163.com
@file: Longest Palindrome.py
@time: 2019/9/4 18:37
@desc: Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.

"""


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        freq_dic = {}
        for w in s:
            if w in freq_dic:
                freq_dic[w] += 1
            else:
                freq_dic[w] = 1
        c = 0
        for key in freq_dic:
            if freq_dic[key] % 2 == 1:
                c += 1
        if c == 0:
            return len(s)
        return len(s) - c + 1
