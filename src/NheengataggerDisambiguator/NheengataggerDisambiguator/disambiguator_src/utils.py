import llist
import pandas as pd
import numpy as np
from .word import *
from .sentence import *
import pathlib

def unique(lst):
    '''
    Returns the unique values of a list, sorted.
    '''
    # initialize a null list
    unique_lst = []
    # traverse for all elements
    for x in lst:
        # check if exists in unique_list or not
        if x not in unique_lst:
            unique_lst.append(x)
    return sorted(unique_lst)

def flatten(lst):
    return [item for sublist in lst for item in sublist]

def resolve_path(p):
    return str(pathlib.Path(p).resolve())



def get_context_from_file_contents(file_contents, tag = None):
    sentences = [strToSentence(s) for s in file_contents.split('\n')]
    context_file = []
    for sentence in sentences:
        for word in sentence:
            # Palavras no início da sentença
            if (word.prev is None) and not (word.next is None):
                context_file.append(Context([None, word.next.getClass()]))
            # Palavras no final da sentença
            elif not (word.prev is None) and (word.next is None):
                context_file.append(Context([word.prev.getClass(), None]))
            # Palavras isoladas
            elif (word.prev is None) and (word.next is None):
                context_file.append(Context([None, None]))
            # Palavras no meio da sentença não isoladas
            else:
                if tag is None:
                    context_file.append(Context([word.prev.getClass(), word.next.getClass()]))
                else:
                    if word is None:
                        print(f'======= aksdhk ===== {word}')
                    if [tag] == word.getClass():
                        context_file.append(Context([word.prev.getClass(), word.next.getClass()]))
    return context_file

def context_table(file_contents, tag):
    def extract_prev():
        context = get_context_from_file_contents(file_contents, tag)
        return list(map(lambda i: str(i.getPrev()), context))
    def extract_next():
        context = get_context_from_file_contents(file_contents, tag)
        return list(map(lambda i: str(i.getNext()), context))
    
    n = len(extract_prev()) 
    data = {
    'tag': [tag for i in range(n)],
    'prev': extract_prev(),
    'next': extract_next()
    }
    return pd.DataFrame(data, columns=['tag','prev','next'])

def myprint(msg):
        if debug:
            print(msg)
