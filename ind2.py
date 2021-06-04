# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 09:55:17 2021

@author: dsd
"""

if __name__ == '__main__':
    wrd = input("Введите предложение: ")
    ans = int(input("Есть ли в предложении запятые(0/1): "))

    cout = wrd.find(",")
    if ans == 0:
        print("0")
    elif ans == 1:
        print(wrd.count("н", 0, cout))