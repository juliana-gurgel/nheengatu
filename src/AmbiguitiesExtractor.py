# -*- coding: utf-8 -*-
# Authors: Juliana Lopes Gurgel <julianalgurgel@alu.ufc.br>
# Last update: July 27, 2023

# This program extracts ambiguities from sentences POS-tagged by Nheengatagger contained in all files in a directory.

# Usage:

# To extract all occurrences of ambiguities from the files:
# ls <path-of-directory> *.txt | xargs -I {} python <path-of-directory> AmbiguitiesExtractor.py {} > file-1.txt

# To sort and delete repeated lines:
# for i in file-1.txt; do sort $i | uniq ; done > file-2.txt

import sys

POStags = ["???", "A", "A2", "ADP", "ADV", "ADVA", "ADVC", "ADVD", "ADVDI", "ADVDX",
           "ADVG", "ADVJ", "ADVL", "ADVLA", "ADVLC", "ADVLT", "ADVM", "ADVNC", "ADVNT",
           "ADVO", "ADVR", "ADVRA", "ADVRC", "ADVRT", "ADVRU", "ADVS", "ADVT", "AFF",
           "ART", "ASSUM", "AUXFR", "AUXFS", "AUXN", "CARD", "CCONJ", "CERT", "CLADP",
           "CLADV", "COND", "CONJ", "CONS", "COP", "CQ", "DEM", "DEMS", "DEMSN", "DEMX",
           "EMP", "EXST", "FOC", "FRUST", "FUT", "IND", "INDQ", "INT", "INTJ", "N", "NEC",
           "NEG", "NEGI", "ORD", "PART", "PFV", "PQ", "PREF", "PREP", "PRET", "PRON", "PRON2",
           "PROPN", "PROTST", "PRSV", "PUNCT", "REL", "RELF", "RPRT", "SCONJ", "SCONJR", "SUFF",
           "TOT", "TOTAL", "V", "V2", "V3", "VSUFF"]


infile = open(sys.argv[1], 'r')

for line in infile:
    words = line.split()
    for word in words:
        ambiguity_sep = "+"
        ambiguities = []
        if ambiguity_sep in word:
            ambiguities.append(word)
        for ambiguity in ambiguities:
            for POS_tag in POStags:
                ambiguities_list = []
                if POS_tag in ambiguity:
                    ambiguity = ambiguity.split('/')
                    ambiguities_list.append(ambiguity[1])
                    for amb in ambiguities_list:
                        print(amb)
