#!/usr/bin/env python3
"""
Author : shelbeezy
Date   : 2019-03-13
Purpose: Sing the bottles of beer on the wall song
"""

import argparse
import sys
import os


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Bottles of beer song',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    #parser.add_argument(
     #   'positional', metavar='str', help='A positional argument')

    parser.add_argument(
        '-n',
        '--num_bottles',
        help='How many bottles',
        metavar='INT',
        type=int,
        default='10')

    return parser.parse_args()


# --------------------------------------------------
def warn(msg):
    """Print a message to STDERR"""
    print(msg, file=sys.stderr)


# --------------------------------------------------
def die(msg='Something bad happened'):
    """warn() and exit with error"""
    warn(msg)
    sys.exit(1)


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    numbottles = args.num_bottles

    while True:
       print('{} bottle{} of beer on the wall,\n{} bottle{} of beer,\nTake one down, pass it around,'.format(numbottles,'' if numbottles==1 else 's', numbottles, '' if numbottles==1 else 's'))
       numbottles -= 1
       print('{} bottle{} of beer on the wall!{}'.format(numbottles, '' if numbottles==1 else 's', '' if numbottles == 0 else '\n'))
       if numbottles == 0:
          break
# --------------------------------------------------
if __name__ == '__main__':
    main()
