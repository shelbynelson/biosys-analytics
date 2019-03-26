#!/usr/bin/env python3
"""
Author : shelbeezy
Date   : 2019-03-25
Purpose: Rock the Casbah
"""

import argparse
import sys
import random
import collections
from itertools import product
# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='"War" cardgame',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        '-s',
        '--seed',
        help='Random seed',
        metavar='int',
        type=int,
        default=None)

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
    seed = args.seed
    suit =list('♥♠♣♦')
    face_val =['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    
    if not seed == None:
       random.seed(seed)
    deck = sorted(product(suit,face_val))
    random.shuffle(deck)
    
    p1_score = 0
    p2_score = 0

    while True:
       if len(deck) == 0:
          break
       p1_card = deck.pop()
       p2_card = deck.pop()
       if p1_card[1] == 'J':
          p1_value = 11
       elif p1_card[1] == 'Q':
          p1_value = 12
       elif p1_card[1] == 'K':
          p1_value = 13
       elif p1_card[1] == 'A':
          p1_value = 14
       else:
          p1_value = int(p1_card[1])
       p1card = p1_card[0]+p1_card[1]
       if p2_card[1] == 'J':
          p2_value = 11
       elif p2_card[1] == 'Q':
          p2_value = 12
       elif p2_card[1] == 'K':
          p2_value = 13
       elif p2_card[1] == 'A':
          p2_value = 14
       else:
          p2_value = int(p2_card[1])
       p2card = p2_card[0]+p2_card[1]		
       if p1_value < p2_value:
          p2_score = p2_score + 1
          winner = 'P2'
       elif p1_value > p2_value:
          p1_score = p1_score + 1
          winner = 'P1'
       else:
          winner = 'WAR!'
       print('{:>3} {:>3} {}'.format(p1card,p2card,winner))			
    print('P1 {} P2 {}: {}'.format(p1_score,p2_score, 'Player 1 wins' if p1_score > p2_score else 'Player 2 wins' if p1_score < p2_score else 'DRAW'))		  


# --------------------------------------------------
if __name__ == '__main__':
    main()
