#!/usr/bin/env python3
"""
Author : shelbeezy
Date   : 2019-04-08
Purpose: Check if a password matches a similar or same password.
"""

import re
import os
import sys


# --------------------------------------------------
def main():
    args = sys.argv[1:]

    if len(args) != 2:
        print('Usage: {} PASSWORD ALT'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    password = args[0]
    alternate = args[1]

    char_check = re.compile('.?'
                         + password
                         + '.?')
  
    if password == alternate or alternate.upper() == password.upper() or char_check.match(alternate):
        print('ok')
    else:
        print('nah')
    


# --------------------------------------------------
main()
