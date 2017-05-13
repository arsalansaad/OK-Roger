# -*- coding: utf-8 -*-
"""
Created on Fri May 12 22:20:26 2017

@author: HP
"""

import sys
from collections import Counter

def cleanser(string):
        return ''.join(e for e in string if e.isalnum())

def word_count(file):
    with open(file) as f:
        content = f.readlines()
    
    content = [x.strip() for x in content]
    content = [item.split(' ') for item in content]
    content = [item for sublist in content for item in sublist]
          
    content = list(map(cleanser,content))
    content = list(filter(None,content))
        
    return Counter(content)
    
def main():
    filename = sys.argv[-1]
    count = word_count(filename)
    for item in count:
        print('{}, {}'.format(item,count[item]))

if __name__ == '__main__':
    main()