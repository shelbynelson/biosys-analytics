#!/usr/bin/env python3
"""
Author : shelbeezy
Date   : 2019-02-22
Purpose: Print the first linesof the contents of each file in a directory.
"""

import argparse
import sys
import os

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Argparse Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'dirname', nargs='+', metavar='DIR', help='Directory name(s)')

    parser.add_argument(
        '-w',
        '--width',
        help='The width of space to print',
        metavar='int',
        type=int,
        default='50')

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
    alldnames = args.dirname
    width = args.width
   
    for dname in alldnames:
      if not os.path.isdir(dname):
          warn('"{}" is not a directory'.format(dname))
          continue
      else:
          d = {}
          print(dname)

          for file in os.listdir(dname):
              line = open(os.path.join(dname, file)).readline().rstrip()
              d[line] = file    
              sorteditems = sorted(d.items())

          for line, file in sorteditems: 
              ellipses = '.'*(width - len(line) - len(file))
              print('{} {} {}'.format(line,ellipses,file))

   
#--------------------------------------------------
if __name__ == '__main__':
    main()
