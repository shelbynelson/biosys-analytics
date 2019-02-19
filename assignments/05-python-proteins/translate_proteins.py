#!/usr/bin/env python3
"""
Author : shelbeezy
Date   : 2019-02-17
Purpose: Translates a given DNA/RNA sequence to amino acids using a provided codon table.
"""

import argparse
import sys
import os


# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Translate DNA/RNA to proteins',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'positional', metavar='STR', help='DNA/RNA sequence')

    parser.add_argument(
        '-c',
        '--codons',
        help='A file with codon translations ',
        metavar='FILE',
        type=str,
        required=True,
        default='None')
        

    parser.add_argument(
        '-o',
        '--outfile',
        help='Output filename ',
        metavar='FILE',
        type=str,
        default='out.txt')

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
    codons = args.codons
    output = args.outfile
    sequence = args.positional.upper()
    seqlength = len(sequence)
    k = 3
    n = seqlength - k + 1
    cdict = {}
    outfile = open(output, 'w')
    
    if not os.path.isfile(codons):
        print('--codons "{}" is not a file'.format(codons))
        sys.exit(1)

    for line in open(codons):
        codon,aminoacids = line.split()
        cdict[codon] = aminoacids

    for i in range(0, n, k):
        codon = sequence[i:i + k]
        if codon in cdict.keys():
             outfile.write(cdict[codon])
        else:
             outfile.write('-')
    outfile.write('\n')
    print('Output written to "{}"'.format(output))   

# --------------------------------------------------
if __name__ == '__main__':
    main()
