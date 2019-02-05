#!/usr/bin/env python3
"""
Author : shelbeezy
Date   : 2019-01-31
Purpose: Allows the user to enter 0...* names and the code will count the number of names
and say hello to each person.
"""

import os
import sys


# --------------------------------------------------
def main():
    names = sys.argv[1:]

    if len(names) == 0:
        print('Usage: {} NAME [NAME...]'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    if len(names) == 1:
        print('Hello to the 1 of you: {}!'.format(names[0])) 
    elif len(names) == 2:
        print('Hello to the 2 of you: {}!'.format(' and '.join(names)))
    elif len(names) > 2:
        lennames = len(names)
        print('Hello to the {} of you: {}'.format(lennames,', '.join(names[0:lennames-1])),end='')
        print(', and {}!'.format(names[lennames-1]))
        

# --------------------------------------------------
main()
