#!/usr/bin/env python3
"""
Author : shelbeezy
Date   : 2019-04-15
Purpose: Calculate the number of edits needed to makde one string the same as a second string
"""

import argparse
import sys
import os
import logging

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Hamming distance',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'FILE', metavar='FILE',nargs = 2, help='File inputs')

    parser.add_argument(
        '-d',
        '--debug',
        help='Debug',
        action='store_true',
        default='False')

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

# -------------------------------------------------
def dist(s1,s2):
    """figures hamming distance between two strings"""
    h_dist = abs(len(s2)-len(s1))

    for letter1, letter2 in zip(s1,s2):
        if letter1 != letter2:
            h_dist += 1
    
    logging.debug('s1 = {}, s2 = {}, d = {}'.format(s1, s2, h_dist)) 

    return h_dist  
# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args() 
    file1, file2 = args.FILE
    hamm_dist = 0

    if not os.path.isfile(file1):
        die('"{}" is not a file'.format(file1))
    if not os.path.isfile(file2):
       die('"{}" is not a file'.format(file2))

    logging.basicConfig(
       filename='.log',
       filemode='w',
       level=logging.DEBUG if args.debug else logging.CRITICAL
    )
    logging.debug('file1 = {}, file2 = {}'.format(file1,file2))
    
    wordf1 = open(file1).read().split()
    wordf2 = open(file2).read().split()

    for s1, s2 in zip(wordf1, wordf2):
       hamm_dist += dist(s1, s2)   
 
    print(hamm_dist)

# --------------------------------------------------
if __name__ == '__main__':
    main()
