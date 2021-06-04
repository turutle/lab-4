# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 10:24:35 2021

@author: dsd
"""

if __name__ == '__main__':
    wrd1 = input("Введите первое слово: ")
    wrd2 = input("Введите второе слово: ")

    for i in range (len(wrd1)):
        ans = wrd1[i] in wrd2
        if ans:
            print("Да")
        else:
            print("Нет")