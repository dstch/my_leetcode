#!/usr/bin/env python
# encoding: utf-8
"""
@author: dstch
@license: (C) Copyright 2013-2019, Regulus Tech.
@contact: dstch@163.com
@file: Best Time to Buy and Sell Stock with Cooldown.py
@time: 2019/9/21 23:04
@desc: Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

    You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
    After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)

Example:

Input: [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]

"""

"""
考虑用动态规划法解决问题，因为当前日期买卖股票的行为会受到之前日期买卖股票行为影响。
对一天的状态有：buy买入，sell卖出，cooldown冷却。
但是对于这一天是否持股只有两种状态：持股状态（buy），没有持股状态（sell，cooldown）。
对于当天持股状态时，至当天的为止的最大利润有两种可能：
1、今天没有买入，跟昨天持股状态一样；
2、今天买入，昨天是冷却期，利润是前天卖出股票时候得到的利润减去今天股票的价钱。 二者取最大值。
对于当天未持股状态，至当天为止的最大利润有两种可能：
1、今天没有卖出，跟昨天未持股状态一样；
2、昨天持有股票，今天卖出了，利润是昨天持有股票时候的利润加上今天股票的价钱。 二者取最大值。
直至最后一天的状态应该是卖出状态。最终利润为sell[n-1];
状态转移方程：
sell[i] = max(sell[i-1], buy[i-1] + price[i]);
buy[i] = max(buy[i-1], sell[i-2] - price[i]);

buy[i]表示在第i天之前最后一个操作是买，此时的最大收益。
sell[i]表示在第i天之前最后一个操作是卖，此时的最大收益。
rest[i]表示在第i天之前最后一个操作是冷冻期，此时的最大收益。
我们写出递推式为：
buy[i]  = max(rest[i-1] - price, buy[i-1]) 
sell[i] = max(buy[i-1] + price, sell[i-1])
rest[i] = max(sell[i-1], buy[i-1], rest[i-1])
上述递推式很好的表示了在买之前有冷冻期，买之前要卖掉之前的股票。一个小技巧是如何保证[buy, rest, buy]的情况不会出现，这是由于buy[i] <= rest[i]， 即rest[i] = max(sell[i-1], rest[i-1])，这保证了[buy, rest, buy]不会出现。
另外，由于冷冻期的存在，我们可以得出rest[i] = sell[i-1]，这样，我们可以将上面三个递推式精简到两个：
buy[i]  = max(sell[i-2] - price, buy[i-1]) 
sell[i] = max(buy[i-1] + price, sell[i-1])

"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        buy, sell, pre_buy, pre_sell = float('-inf'), 0, 0, 0
        for price in prices:
            pre_buy = buy
            buy = max(pre_buy, pre_sell - price)
            pre_sell = sell
            sell = max(pre_sell, pre_buy + price)
        return sell
