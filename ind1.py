# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 09:31:28 2021

@author: dsd
"""

if __name__ == '__main__':
    wrd = input("Введите предложение: ")
    smb = input("Введите символ: ")
    
    cout = wrd.count(smb)
    while cout > 0:
        print(smb)
        cout =- 1