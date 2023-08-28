'''This program translates from Portuguese or French to English sentences of the following source:

TREVISAN, Rodrigo Godinho. Tradução comentada da obra Le Petit Prince, de Antoine de Saint-Exupéry, do francês ao nheengatu. 2017.
Dissertação (Mestrado) – Universidade de São Paulo, São Paulo, 2017.
Available at: http://www.teses.usp.br/teses/disponiveis/8/8160/tde-07082017-124328/. Acesso em: 25 maio 2023. 

Autor: Juliana Lopes Gurgel <julianagurgel@letras.ufc.br>
Last update: August 22, 2023

'''

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

#infilename = input("File: ")
#infile = open(infilename, 'r').read().splitlines()

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
