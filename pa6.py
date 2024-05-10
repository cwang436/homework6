#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  9 17:25:30 2024

@author: charliewang

this is the code for pa6
"""


def make_change(total):
    '''makes all possible change combos'''
    coins = [1, 5, 10, 25, 100]
    result = []
    helperchange(total, coins, [], result)
    return result


def helperchange(remaining, coins, current_combo, result):
    '''helper for make_change'''
    if remaining == 0:
        result.append(list(current_combo))
        return
    if len(coins) == 0:
        return
    coin = coins[0]
    max_coins = remaining // coin
    for i in range(max_coins + 1):
        helperchange(remaining - i * coin, coins[1:],
                     current_combo + [coin] * i, result)


def dict_filter(func, dictionary):
    '''filters a dictionary through a given function'''
    ret = {}
    for key, val in dictionary.items():
        if func(key, val) is True:
            ret[key] = val
    return ret


def treemap(function, tree):
    '''puts all keys and values of a tree through a given function'''
    tree.key, tree.value = function(tree.key, tree.value)
    for i in tree.children:
        treemap(function, i)


class DTree:
    '''decision tree class'''

    def __init__(self, variable, threshold, lessequal, greater, outcome):
        '''constructor'''
        if (variable is None or threshold is None or lessequal is None or greater is None) == (outcome is None):
            raise ValueError()
        self.variable = variable
        self.threshold = threshold
        self.lessequal = lessequal
        self.greater = greater
        self.outcome = outcome

    def tuple_atleast(self):
        '''at least how many values required in the tuple'''
        if self.variable is None:
            return 0
        maxnum = self.variable + 1
        if self.lessequal.tuple_atleast() > maxnum:
            maxnum = self.lessequal.tuple_atleast()
        if self.greater.tuple_atleast() > maxnum:
            maxnum = self.greater.tuple_atleast()
        return maxnum

    def find_outcome(self, tple):
        '''finds decision given tuple with data'''
        if self.variable is None:
            return self.outcome
        if tple[self.variable] > self.threshold:
            return self.greater.find_outcome(tple)
        if tple[self.variable] <= self.threshold:
            return self.lessequal.find_outcome(tple)

    def no_repeats(self):
        '''determines if there repeated tests in decision tree'''
        def helper(node, lst):
            if node.variable is None:
                return True
            if node.variable in lst:
                return False
            lst.append(node.variable)
            return helper(node.lessequal, lst) and helper(node.greater, lst)
        return helper(self, [])
