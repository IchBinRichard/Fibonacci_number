#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 15:43:27 2022

@author: lijiaheng
"""

#費波那契數列
# F0 = 0; F1 = 1, Fn = (Fn - 1) + (Fn - 2) while n >= 2

def fib (n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
    
n = int(input('請輸入n值：'))
print('當 n 為', n, '時，費波那契數為：', fib(n))
    



        
    
    
    
    
    
    
    
    