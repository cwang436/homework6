#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  9 17:25:30 2024

@author: charliewang

this is the code for pa6
"""

         
def make_change(total):
    coins = [1, 5, 10, 25, 100]
    result = []
    helperchange(total, coins, [], result)
    return result

def helperchange(remaining, coins, current_combo, result):
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

total = 10
print(make_change(total))


def dict_filter(func, dictionary):
    ret = {}
    for key, val in dictionary.items():
        if func(key, val) is True:
            ret[key] = val
    return ret


example = {"Illinois": "IL", "Pennsylvania": "PA", "Indiana": "IN"}
def checker(name, abbrev):
    return abbrev[0] == "I" and name[1] == "l"
print(dict_filter(checker, example))


class KVTree:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.children = []
    def add_child(self, child):
        self.children.append(child)
samplekv = KVTree("us", 4.6)
pa = KVTree("pa", 1.9)
samplekv.add_child(pa)
pa.add_child(KVTree("Pittsburgh", 0.3))
pa.add_child(KVTree("Philadelphia", 1.6))
il = KVTree("il", 2.7)
samplekv.add_child(il)
il.add_child(KVTree("Chicago", 2.7))

def treemap(function, tree):
    tree.key, tree.value = function(tree.key, tree.value)
    for i in tree.children:
        treemap(function, i)

treemap(lambda x, y: (x.upper(), y * 1000000), samplekv)
