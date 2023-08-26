"""Nheengatagger Disambiguator

Usage:
  desambiguador [--log-level=<log-level>] contexto <corpus> <tagset> --out <contexto>
  desambiguador [--log-level=<log-level>] sentenca <sentenca> --contexto <ctx>

Options:
  -h --help     Show this screen.
  --version     Show version.
"""
from docopt import docopt
import sys
import os
import logging
from pathlib import Path

import pandas as pd
import numpy as np


from .utils import *
import disambiguator_src.word as wd
import disambiguator_src.sentence as st
import disambiguator_src.context as ctx
import disambiguator_src.corpus as crp
import disambiguator_src.disambiguator as ds

log_levels = {
    'DEBUG': 0,
    'INFO': 1,
    'WARNING': 2,
    'ERROR': 3,
    'CRITICAL': 4
}

def cli():
    arguments = docopt(__doc__, version='Nheengatagger Disambiguator 1.5: fix frequency in Context Table')

    if arguments['--log-level'] != None:
        numeric_level = log_levels[arguments['--log-level']]
        if not isinstance(numeric_level, int):
            raise ValueError('Invalid log level: %s' % loglevel)
        log_file = pathlib.Path('/home/juliana/complin/nheengatu/src/NheengataggerDisambiguator','disambiguator.log')
        logging.basicConfig(filename=log_file, filemode='w', level=numeric_level)

    if arguments['contexto']:
        assert pathlib.Path(arguments['<corpus>']).exists(), 'Diretório não existe'
        assert pathlib.Path(arguments['<tagset>']).exists(), 'Arquivo não existe'

        # Leitura do corpus
        corpus = crp.read_corpus(resolve_path(Path(arguments['<corpus>'])))

        # Leitura da lista de etiquetas
        tagset_tbl = pd.read_excel(resolve_path(Path(arguments['<tagset>'])))
        tagset = np.unique(list(tagset_tbl['tag'])).tolist()

        freq = ctx.context(tagset, corpus)
        freq.to_csv(arguments['<contexto>'], index = False)
        
#    if arguments['corpus']:
#        assert pathlib.Path(arguments['<corpus>']).exists(), 'Diretório não existe'
#        assert pathlib.Path(arguments['<ctx>']).exists(), 'Arquivo não existe'
#                
#
#        # Leitura do corpus
#        corpus = crp.read_corpus2(resolve_path(pathlib.Path(arguments['<corpus>'])))
#        freq = pd.read_csv(resolve_path(Path(arguments['<ctx>'])))
#        
#        ds.disambiguate_corpus(corpus, freq)
                
    if arguments['sentenca']:
        assert arguments['<sentenca>'] != '', 'Sentença vazia'
        assert pathlib.Path(arguments['<ctx>']).exists(), 'Arquivo não existe'

        freq = pd.read_csv(resolve_path(Path(arguments['<ctx>'])))
        s = ds.disambiguate_sentence(arguments['<sentenca>'], freq)
        #" ".join([f'{w[0]}/{"+".join(w[1])}' for w in sentence])
        print(s)
        #print(" ".join([f'{w[0]}/{"+".join(w[1])}' for w in s]))
        #print(s.split(" "))
