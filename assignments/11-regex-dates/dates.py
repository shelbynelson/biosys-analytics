#!/usr/bin/env python3
"""
Author : shelbeezy
Date   : 2019-04-01
Purpose: Uses regular expression to convert dates into a standard date
"""

import os
import sys
import re

# --------------------------------------------------
def main():
    args = sys.argv[1:]

    if len(args) == 0:
        print('Usage: {} DATE'.format(os.path.basename(sys.argv[0])))
        sys.exit(1)

    date = args[0]
    #year_arg = args[1]
    
    date_re1 = re.compile('(?P<year>\d{4})'
                          '[-]?'
                          '(?P<month>\d{1,2})'
                          '[-]?'
                          '(?P<day>\d{0,2})')

    date_re2 = re.compile('(?P<month>\d{1,2})'
                          '[/]'
                          '(?P<year>\d{1,2})')
    
    date_re3 = re.compile('(?P<month>[a-z]{1,10})'
                          '[-,]?'
                          '(\s*)?'
                          '(?P<year>\d{4})')

    
    match1 = date_re1.match(date) 
    match2 = date_re2.match(date)
    match3 = date_re3.match(date)
    match = match1 or match2 or match3
    #months = match.group('month')
   # print(months) 
   #print(match1.group('month'))
    #print(match1.group('day'))
    if match == match1 and match1 != None:
        if len(match1.group('month')) == 1:
            month = '0' + match1.group('month')
        elif len(match1.group('month')) == 2:
            month = match1.group('month')

        if len(match1.group('day')) == 1:
            day = '0' + match1.group('day')
        elif len(match1.group('day')) == 2:
            day = match1.group('day')
        else:
            day = '01'

        standard = '{}-{}-{}'.format(match1.group('year'), month, day)
        
    elif match == match2 and match2 != None:
        if len(match2.group('month')) == 1:
            month = '0' + match2.group('month')
        elif len(match2.group('month')) == 2:
            month = match2.group('month')

        standard = '{}-{}-{}'.format('20'+ match2.group('year'), month, '01')
        
    elif match == match3 and match3 != None:
        standard = '{}-{}-{}'.format(match3.group('year'), match3.group('month'), '01')
    else:
        standard = 'No match'
    print(standard)
 
# --------------------------------------------------
main()
