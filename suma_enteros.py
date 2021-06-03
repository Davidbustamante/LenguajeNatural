#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 18:18:16 2019

@author: davidbellobustamante
"""

def sumatoria(X, num):
 if(num > 0):
  X = sumatoria(X, num-1)
  X = X + num
  return X
 else:
  X = 0
 return X
X = 0
num = int(input("Ingresa un número entero\n"))
X = sumatoria(X, num)
print(X)