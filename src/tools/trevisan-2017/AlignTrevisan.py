# -*- coding: utf-8 -*-
# Authors: Juliana Lopes Gurgel <julianagurgel@letras.ufc.br>
# Last update: May 25, 2023

# This program extracts ambiguities from sentences POS-tagged by Nheengatagger contained in all files in a directory.

# Usage in Linux command line:

# for i in <path-of-directory> *.txt; do python <path-of-directory>/AlignTrevisan.py $i > ${i%normalized.txt}aligned.txt ; done

import sys

infile = open(sys.argv[1], "r", encoding="utf-8")
lines = infile.read().splitlines()

count = 0
l_odd = list()
l_even = list()
yrl_fr = list()
for line in lines[1:]:
    count = count + 1
    even = count % 2 == 0
    odd = count % 2 != 0
    if odd:
        odd = line
        l_odd.append(str(count + 1) + ' ' + odd)

    else:
        even = line
        l_even.append(str(count -1) + ' ' + even)

for i in l_odd:
    words = i.split()
    yrl_fr.append(words)

for i in l_even:
    words = i.split()
    yrl_fr.append(words)

l = list()
for i in yrl_fr:
    num = int(i[0])
    s = i[3:]
    tup = (num, s)
    l.append(tup)
    l = sorted(l)

for k,v in l:
    sentence = i[3:]
    if k % 2 != 0:
        print(' '.join(v))
    else:
        print(' '.join(v), '\n')
