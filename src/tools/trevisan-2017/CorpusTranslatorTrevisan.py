# -*- coding: utf-8 -*-
# Authors: Juliana Lopes Gurgel <julianagurgel@letras.ufc.br>
# Last update: August 30, 2023

# This program extracts ambiguities from sentences POS-tagged by Nheengatagger contained in all files in a directory.

# Usage in Linux command line:

# for i in <path-of-directory> *.txt; do python <path-of-directory>/CorpusTranslatorTrevisan.py $i > ${i%aligned.txt}yrl-por-eng-fra.txt ; done

#This program translates sentences from French to Portuguese and English, of the following source:

# TREVISAN, Rodrigo Godinho. Tradução comentada da obra Le Petit Prince, de Antoine de Saint-Exupéry, do francês ao nheengatu. 2017.
# Dissertação (Mestrado) – Universidade de São Paulo, São Paulo, 2017.
# Available at: http://www.teses.usp.br/teses/disponiveis/8/8160/tde-07082017-124328/. Acesso em: 25 maio 2023.

from deep_translator import GoogleTranslator
import sys, datetime

infilename = open(sys.argv[1], "r", encoding="utf-8")
infile = infilename.read().splitlines()

header = print(f"""'''This text file contains aligned sentences in Nheengatu, Portuguese, English and French from the following source:

TREVISAN, Rodrigo Godinho. Tradução comentada da obra Le Petit Prince, de Antoine de Saint-Exupéry, do francês ao nheengatu. 2017.
Dissertação (Mestrado) – Universidade de São Paulo, São Paulo, 2017.
Available at: http://www.teses.usp.br/teses/disponiveis/8/8160/tde-07082017-124328/. Acesso em: 25 maio 2023. 

Therefore, this data may be subject to copyrights of the author of this book.

Producer: Juliana Lopes Gurgel
Produced: June 12, 2023

Automatically translated from French to Portuguese and English by CorpusTranslator.
Translated: {datetime.datetime.now().strftime("%c")}.
Translation reviewer: TODO
Reviewed: TODO'''""", '\n')

include=True
count = 0
for line in infile:
    line = line.replace('# ', '')
    line = line.rstrip()
    # Ignore the header of the file
    if line.startswith("'''"):
        include=False
    elif line.endswith("'''"):
        include=True
    else:
        if include:
            if line:
                count = count +1
                # Find and print all Nheengatu sentences (count = odd number)
                if count % 2 != 0:
                    print(line)
                # Find and print all Portuguese sentences (count = even number)
                else:
                    # Translate Portuguese sententes to English
                    fr_por = GoogleTranslator(source='fr', target='pt').translate(line)
                    fr_en = GoogleTranslator(source='fr', target='en').translate(line)
                    #print(header, '\n')
                    # Comment and print and all Portuguese sentences
                    print('#', fr_por)
                    # Comment and print and all English sentences
                    print('#', fr_en)
                    # Comment and print all French sentences
                    print('#', line, '\n')
