#!/usr/bin/env python3
"""
Author : shelbeezy
Date   : 2019-02-04
Purpose: This code recieves a string and counts the number of vowels in the string.
"""

import os
import sys


# --------------------------------------------------
def main():
    phrase = sys.argv[1:]
    #word = phrase[0]
    vcount = 0
    i = 0
    if len(phrase) == 0:
        print('Usage: {} STRING'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)
    elif len(phrase) >= 1:
        word = phrase[0]
        for i in word:
           if(i=='A' or i=='a' or i=='E' or i=='e' or i=='I' or i=='i' or i=='O' or i=='o' or i=='U' or i=='u'):
               vcount = vcount+1
        if vcount == 0:
            print('There are 0 vowels in "{}."'.format(word))
        elif vcount == 1:
            print('There is 1 vowel in "{}."'.format(word))
        elif vcount > 1:
            print('There are {} vowels in "{}."'.format(vcount,word))
        
# --------------------------------------------------
main()
