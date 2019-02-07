#!/usr/bin/env python3
"""
Author : shelbeezy
Date   : 2019-02-06
Purpose: Place numbers and colon in front of each line in a text file.
"""

import os
import sys


# --------------------------------------------------
def main():
    args = sys.argv[1:]

    if len(args) != 1:
        print('Usage: {} FILE'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)
    
    file = args[0]
    
    if not os.path.isfile(file):
        print('{} is not a file'.format(file))
        sys.exit(1)
    i = 0
    for line in open(file):
        i = i + 1
        print('    {}: {}'.format(i, line),end='')


# --------------------------------------------------
main()
