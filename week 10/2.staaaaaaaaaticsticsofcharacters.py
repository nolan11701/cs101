# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 09:56:14 2021

@author: nolan
"""

johncena = input()
jomama = len([x for x in johncena if x.isalpha()])
poo = len([x for x in johncena if x.isnumeric()])
pickles = len(johncena)-poo-jomama-1
print("Letters=",jomama,sep = "")
print("Digits=",poo,sep = "")
print("Others=",pickles,sep = "")