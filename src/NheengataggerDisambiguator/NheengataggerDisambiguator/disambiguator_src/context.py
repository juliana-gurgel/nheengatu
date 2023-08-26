import pandas as pd
import numpy as np
from .utils import flatten

import disambiguator_src.sentence as st
import disambiguator_src.word as wd

def context_per_tag(tag, corpus):
    '''
    Retorna a tabela de contexto para uma única etiqueta TAG presente no CORPUS.
    '''
    res = []

    corpus_reduced = list(filter(lambda x: st.has_tag(x, tag), [st.tokenize(s) for s in corpus]))    
    for sentence in corpus_reduced:
        nwords = len(sentence)
        for i in range(len(sentence)):
            word = sentence[i]
            if not wd.is_ambiguous(word):
                if tag in wd.tags(word):                    
                    for prev_next in ['prev', 'next']:
                        neighbor_idx = i-1 if prev_next == 'prev' else i+1
                        if neighbor_idx < 0 or neighbor_idx >= nwords:
                            res.append([tag, prev_next, 'None'])
                        else:
                            neighbor = sentence[neighbor_idx]
                            if not wd.is_ambiguous(neighbor):
                                for t in wd.tags(neighbor):
                                    if t == 'e': 
                                        print(sentence)
                                    res.append([tag, prev_next, t])
    return res

def context(tagset, corpus):
    '''
    Retorna a tabela de contexto para as etiquetas de TAGSET presentes no CORPUS.
    '''
    res = []
    
    # Create the pandas DataFrame
    df = pd.DataFrame(
        flatten(
            [context_per_tag(t, corpus) for t in tagset]
        )
    )
    # specifying column names
    df.columns = ['tag', 'prev_next', 'pos_tag']
    
    for prev_next in ['prev', 'next']:
        x = df[df.prev_next == prev_next].groupby(['tag', 'pos_tag']).count()
        x.reset_index(inplace = True)
        if x.shape[0] > 0:
            x.columns = ['tag', 'pos_tag', 'frequency']
            x['prev_next'] = prev_next
            res.append(x[['tag', 'pos_tag', 'prev_next', 'frequency']]) 
    return pd.concat(res)

