# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 10:01:02 2021

@author: dsd
"""

if __name__ == '__main__':
    word = input("Введите слово: ")
    
    idx = len(word) // 2
    if len(word) % 2 == 1:
        # Длина слова нечетная.
        r = word[:idx] + word[idx+1:]
    else:
        # Длина слова четная.
        r = word[:idx-1] + word[idx+1:]
        
    print(r)