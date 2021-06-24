# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 10:18:58 2021

@author: dsd
"""

if __name__ == '__main__':
    sent = input("Введите предложение: ")
    wrd = input("Введите слово: ")
    ans = sent.count(wrd)
    for i in range(ans):
        print(wrd)