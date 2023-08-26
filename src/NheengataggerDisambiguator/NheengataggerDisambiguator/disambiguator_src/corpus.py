import os
import logging
import disambiguator_src.sentence as st
from .utils import flatten

def read_tagged_file(filePath):
    with open(filePath, 'r', encoding='utf-8') as fp:
        lines = fp.readlines()
        res = []
        include=True
        for line in lines:
            line=line.strip()
            if line.startswith("'''"):
                include=False
            elif line.endswith("'''"):
                include=True
            else:
                if include and not line.startswith("#"):
                    if line:
                        res.append(line)
        return('\n'.join(res))

def read_corpus(corpus_dir):
    
    logging.info(f'Lendo corpus do diretório {corpus_dir}')
    res = []
    for file in os.listdir(corpus_dir):
        file_contents = read_tagged_file(f'{corpus_dir}/{file}')
        res.append(file_contents.split("\n"))
    return flatten(res)

def read_corpus2(corpus_dir):
    logging.info(f'Lendo corpus do diretório {corpus_dir}')
    res = dict()
    corpus_files = os.listdir(corpus_dir)    
    for file in corpus_files:
        file_contents = read_tagged_file(f'{corpus_dir}/{file}')
        res[file] = file_contents
    return res


def corpus_contents(corpus):
    '''
    Returns a list containing all the sentences within the corpus
    '''
    lst = flatten([file_contents.split('\n') for file_contents in corpus.values()])
    sentences = [st.tokenize(s) for s in lst]
    return sentences
