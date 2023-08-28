# -*- coding: utf-8 -*-
# Authors: Juliana Lopes Gurgel <julianagurgel@letras.ufc.br>
# Last update: June 19, 2023

# This program extracts ambiguities from sentences POS-tagged by Nheengatagger contained in all files in a directory.

# Usage in Linux command line:

# for i in <path-of-directory> *.txt; do python <path-of-directory>/AlignTrevisan.py $i > ${i%.txt}-aligned.txt ; done

import sys

infilename = open(sys.argv[1], "r", encoding="utf-8")
infile = infilename.read().splitlines()

def normalize(infile):
    while True:
        try:
            for line in infile:
                line = line.rstrip()
                num = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
                if line.startswith(num):
                    start = print('\n', line, end='')
                elif not line.startswith(num):
                    end = print('', line, end=' ')
            break
        except:
            break
            
out = normalize(infile)
print(out)


##import sys
##
##infilename = open(sys.argv[1], "r", encoding="utf-8")
##infile = infilename.read().splitlines()
##
##def normalize(infile):
##    while True:
##        try:
##            for line in infile:
##                line = line.rstrip()
##                num = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
##                if line.startswith(num):
##                    if num == '1':
##                        start = print('', line, end='')
##                    if num != '1':
##                        start = print('\n', line, end='')
##                elif not line.startswith(num):
##                    end = print('', line, end=' ')
##            break
##        except:
##            break
##            
##print(normalize(infile))
