#!/usr/bin/env python3
"""
Author : shelbeezy
Date   : 2019-02-06
Purpose: Prints the first three lines of a text file, 
but user can enter the desired number.
"""

import os
import sys


# --------------------------------------------------
def main():
    args = sys.argv[1:]

    if len(args) == 0:
        print('Usage: {} FILE [NUM_LINES]'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    file = args[0]
    numlines = 3
    i = 0

    if not os.path.isfile(file):
        print('{} is not a file'.format(file))
        sys.exit(1)
    
    if len(args) == 2:
        numlines = int(args[1])
        if numlines <= 0:
            print('lines ({}) must be a positive number'.format(numlines))
            sys.exit(1) 

    for line in open(file):
        i = i + 1
        print('{}'.format(line),end='') 
        if i == numlines:
            break
        


# --------------------------------------------------
main()
