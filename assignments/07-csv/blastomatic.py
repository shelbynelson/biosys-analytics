#!/usr/bin/env python3
"""
Author : shelbeezy
Date   : 2019-03-13
Purpose: Parsing a CSV file
"""

import csv
import argparse
import sys
import os
from collections import defaultdict

# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Annotate BLAST output',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'mainfile', metavar='FILE', help='BLAST output (-outfmt 6)')

    parser.add_argument(
        '-a',
        '--annotations',
        help='Annotation file',
        metavar='FILE',
        type=str,
        default='')

    parser.add_argument(
        '-o',
        '--outfile',
        help='Output file',
        metavar='FILE',
        type=str,
        default='')

    
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
    main_file = args.mainfile
    anno_file = args.annotations
    out_file = args.outfile
  
    if not os.path.isfile(main_file):
        die('"{}" is not a file'.format(main_file))
    if not os.path.isfile(anno_file):
        die('"{}" is not a file'.format(anno_file))
   
    lookup={}
    with open(anno_file) as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for row in reader:
           lookup[row['centroid']]=row
    
    out_f = open(out_file, 'wt') if out_file else sys.stdout
    out_f.write('\t'.join(['seq_id', 'pident', 'genus', 'species']) +'\n')
    
    with open(main_file) as csvfile:
        reader = csv.DictReader(csvfile, delimiter='\t', fieldnames=('qaccver', 'saccver', 'piednt', 'length', 'mismatch', 'gapopen', 'qstart', 'qend', 'sstart', 'send', 'evalue', 'bitscore'))
        for row in reader:
           seq_id = row['sseqid']
           if seq_id not in lookup:
              warn('Cannot find seq "{}" in lookup'.format(seq_id))
              continue




# --------------------------------------------------
if __name__ == '__main__':
    main()
