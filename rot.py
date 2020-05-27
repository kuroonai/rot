#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 11:38:58 2020

@author:Naveen Kumar Vasudevan, 
        400107764,
        Doctoral Student, 
        The Xi Research Group, 
        Department of Chemical Engineering,
        McMaster University, 
        Hamilton, 
        Canada.
        
        naveenovan@gmail.com
        https://naveenovan.wixsite.com/kuroonai
"""
'''

Usage: 
    python rot.py <file_to_crytpted_or_decrpted> <crypt or decrypt> <rot number>
    
    eg: python rot.py text.dat crypt 13
    
'''

import string
import sys

data = sys.argv[1]

#crypt = 1
if sys.argv[2] == 'crypt': crypt = 1
elif sys.argv[2] == 'decrypt': crypt = 0
else: raise Exception('crypt or decrypt')

rotnum = int(sys.argv[3])
#rotnum = 13


actual = list(string.ascii_letters)
ciphered = list(actual[rotnum:] + actual[:rotnum])


with open(data, 'r') as file:
    inp = file.read() #.replace('\n', ' ')

split_inp = inp.split()
out = ''

for iind, i in enumerate(split_inp):
    letters = list(i)
    
    newword = ''
    for  j in letters:
        if crypt == True:
            if j in ciphered:newword += actual[ciphered.index(j)]
            else : newword += j
        else:
            if j in actual:newword += ciphered[actual.index(j)]
            else : newword += j
    if iind != 0: out += ' '
    out += newword

with open('output_file.txt','w') as oup:
    oup.write(out)
    
print(out)       
        
    