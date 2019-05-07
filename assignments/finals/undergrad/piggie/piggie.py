#!/usr/bin/env python3
"""
Author : shelbeezy
Date   : 2019-05-07
Purpose: Converts words to pig latin
"""

import argparse
import sys
import os
import re
import string


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Convert to Pig Latin',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'wordString', metavar='STR', help='Input text or file')

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
    phrase = args.wordString
    
    if os.path.isfile(phrase):
        with open(phrase) as filename:
            for row in filename:
               
               line = row.split()
               for word in line:
                  char = re.sub("[^a-zA-Z0-9']", '', word)
                  consonants = re.sub('[aeiouAEIOU]', '', string.ascii_letters)
                  match = re.match('^([' + consonants + ']+)(.+)', char)

                  if match:
                     print('-'.join([match.group(2), match.group(1) + 'ay ']),end="")
                  else:
                     print(char + '-yay ', end ="")

               print("\n", end="")



    else:
       line = phrase.split()
       
    for word in line:
       char = re.sub("[^a-zA-Z0-9']", '', word)
       consonants = re.sub('[aeiouAEIOU]', '', string.ascii_letters)
       match = re.match('^([' + consonants + ']+)(.+)', char)
       
       if match:
           print('-'.join([match.group(2), match.group(1) + 'ay ']),end="")
       else:
           print(char + '-yay ', end ="")

    print("\n")
# --------------------------------------------------
if __name__ == '__main__':
    main()
