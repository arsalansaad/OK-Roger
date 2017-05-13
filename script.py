# -*- coding: utf-8 -*-
"""
Created on Fri May 12 22:20:26 2017

@author: HP
"""

import sys
import argparse
from collections import Counter

def cleanser(string):
        return ''.join(e for e in string if e.isalnum())

def word_count(file,case):
    with open(file) as f:
        content = f.readlines()
    
    content = [x.strip() for x in content]
    content = [item.split(' ') for item in content]
    content = [item for sublist in content for item in sublist]
          
    content = list(map(cleanser,content))
    content = list(filter(None,content))
    
    if case:
        content = [x.lower() for x in content]
    return Counter(content)
    
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    parser.add_argument('-i',help='Ignores Case while counting words',action='store_true',dest='ignore')
    args = parser.parse_args()
    filename = args.filename
    if args.ignore:
        count = word_count(filename,True)
    else:
        count = word_count(filename,False)
    for item in count:
        print('{}, {}'.format(item,count[item]))
    print(len(count))

if __name__ == '__main__':
    main()