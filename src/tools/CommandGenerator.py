# -*- coding: utf-8 -*-

# Authors: Juliana Lopes Gurgel <julianalgurgel@alu.ufc.br>
# Last update: July 29, 2023

# This program generates commands to extract sentences in Nheengatu 
# with occurrences of POS-tags or ambiguities and to count these occurrences 
# in text files automatically POS-tagged by Nheengatagger.

# Nheengatagger available at: https://github.com/CompLin/nheengatu/tree/main/src

POStags = ["???", "A", "A2", "ADP", "ADV", "ADVA", "ADVC", "ADVD", "ADVDI", "ADVDX",
           "ADVG", "ADVJ", "ADVL", "ADVLA", "ADVLC", "ADVLT", "ADVM", "ADVNC", "ADVNT",
           "ADVO", "ADVR", "ADVRA", "ADVRC", "ADVRT", "ADVRU", "ADVS", "ADVT", "AFF",
           "ART", "ASSUM", "AUXFR", "AUXFS", "AUXN", "CARD", "CCONJ", "CERT", "CLADP",
           "CLADV", "COND", "CONJ", "CONS", "COP", "CQ", "DEM", "DEMS", "DEMSN", "DEMX",
           "EMP", "EXST", "FOC", "FRUST", "FUT", "IND", "INDQ", "INT", "INTJ", "N", "NEC",
           "NEG", "NEGI", "ORD", "PART", "PFV", "PQ", "PREF", "PREP", "PRET", "PRON", "PRON2",
           "PROPN", "PROTST", "PRSV", "PUNCT", "REL", "RELF", "RPRT", "SCONJ", "SCONJR", "SUFF",
           "TOT", "TOTAL", "V", "V2", "V3", "VSUFF"]

ambiguities = ["A2\+ADVS","A2\+N","A\+A2","A\+A2\+ADV","A\+ADVA","A\+ADVA\+N","A\+ADVC",
               "A\+ADVC\+N","A\+ADV\+N","A\+ADVS","A\+ADVS\+INDQ","ADP\+ADVA\+IND","ADP\+ADVG",
               "ADP\+FUT\+SCONJ","ADP\+N","ADP\+N\+SCONJ","ADP\+SCONJ","ADV\+CCONJ\+V","ADVDI\+ADVJ",
               "ADVDX\+DEMX\+V","ADVJ\+ADVT","ADVJ\+CCONJ","ADVJ\+SCONJR","ADVLA\+ADVRA\+SCONJR",
               "ADVLC\+ADVNC\+ADVRC","ADVLC\+ADVRC","ADVM\+ADVT","ADVNT\+ADVRT\+SCONJR","ADVO\+ORD",
               "ADVS\+INDQ","ADVT\+CCONJ","A\+INDQ","A\+INTJ\+N","A\+N","A\+N\+V2","A\+PRET",
               "ART\+CARD\+FRUST\+SCONJ","A\+V","A\+V2","CARD\+INDQ","CERT\+N","CLADP\+PRON2",
               "COND\+IND\+INT\+N\+REL\+V","DEMSN\+PRON","FOC\+NEGI","FOC\+PREP\+SCONJR","IND\+INT\+RELF",
               "IND\+NEG","INDQ\+INT\+TOT","N\+REL","N\+V","N\+V2","PRON\+PRON2","TOT\+TOTAL\+V","V\+V2"]

print('''
Usage:

Type 'tagset' if you want to generate commands for all POS-tags in ambiguous and non-ambiguous words.

Type 'POS-tag' if you want to generate a command for one specific POS-tag in ambiguous and non-ambiguous words.

Type 'ambiguities' if you want to generate commands for all ambiguities.

Type 'count POS-tags' if you want to generate commands to count the occurrences of all POS-tags.

Type 'count ambiguities' if you want to generate commands to count the occurrences of all ambiguities.
''')

while True:
    inpt = input('>>> ')
    try:
        if inpt == 'tagset':
            for POS_tag in POStags:
                print(f"grep -E '(/{POS_tag}+[[:space:]]|/{POS_tag}\+|\+{POS_tag}\+|\+{POS_tag}+[[:space:]])' *pos.txt > /home/juliana/complin/nheengatu/data/corpus/navarro-2016/corpus/occurrences_POStagset/{POS_tag}_occurrences.txt")
            break
        if inpt == 'POS-tag':
            print('\n','Tagset:','\n\n', POStags, '\n')
            POS_tag = input('>>> Type a POStag: ')
            if POS_tag in POStags:
                print(f"\ngrep -E '(/{POS_tag}+[[:space:]]|/{POS_tag}\+|\+{POS_tag}\+|\+{POS_tag}+[[:space:]])' *pos.txt  > /home/juliana/complin/nheengatu/data/corpus/navarro-2016/corpus/occurrences_POStag/{POS_tag}_occurrences.txt")
            break
        if inpt == 'ambiguities':
            for ambiguity in ambiguities:
                print(f"grep -E '(/{ambiguity}+[[:space:]])' *pos.txt  > /home/juliana/complin/nheengatu/data/corpus/navarro-2016/corpus/occurrences_ambiguities/{ambiguity}_occurrences.txt")
            break
        if inpt == 'count POS-tags':
            for POS_tag in POStags:
                print(f"""echo "$(grep -R /{POS_tag}\\  | wc -l) matches in $(grep -Rl /{POS_tag}\\  | wc -l) *pos.txt\"""")
            break
        if inpt == 'count ambiguities':
            for ambiguity in ambiguities:
                print(f"""echo "$(grep -R /{ambiguity}\\  | wc -l) matches in $(grep -Rl /{ambiguity}\\  | wc -l) *pos.txt\"""")
            break
    except:
        print('\nInvalid input')
        continue
