# -*- coding: utf-8 -*-
"""
Created on Sat May 13 12:36:37 2017

@author: HP
"""

import pickle
import re
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
    
def search(prefix,count):
    lst = []
    pat = '^'+prefix
    for item in count:
        match = re.search(pat,item)
        if match:
           lst.append(item) 
    return lst
    
    
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('prefix',action='store')
    parser.add_argument('-i',help='Ignores Case while counting words',action='store_true',dest='ignore')
    args = parser.parse_args()
    prefix = args.prefix
    if args.ignore:
        file = 'count_ignore.txt'
    else:
        file = 'count.txt'
    with open(file, "rb") as myFile:
        count = pickle.load(myFile)
    matches = search(prefix,count)
    for item in matches:
        print('{}, {}'.format(item,count[item]))

if __name__ == '__main__':
    main()