# -*- coding: utf-8 -*-
# Authors: Juliana Lopes Gurgel <julianagurgel@letras.ufc.br>
# Last update: August 30, 2023

# This program aims to extract sentences in nheengatu from Conllu format into sentences POS-tagged with Nheengatagger Tagset.
# Potentially, it is possible to extract sentences in any language from Conllu format into sentences POS-tagged with UD Tagset or the tagset of that specific language.

# Usage in Linux command line:

# for i in <path-of-directory> *.txt; do python <path-of-directory>/ConlluSentExtractor.py $i > ${i%.txt}POStaggedSentences.txt ; done

from conllu import *
import sys

data = open(sys.argv[1], 'r', encoding='utf-8')
data = data.read()

def POStaggedSentence(conllu_sentences):
    sentences = parse(conllu_sentences)
    for sentence in sentences:
        words = [token['form'] for token in sentence]
        tags = [token['xpos'] for token in sentence]
        for word, tag in zip(words, tags):
            print(word, tag, sep= "/", end=' ')
        print('\n', end='')

POStaggedSentence(data)





