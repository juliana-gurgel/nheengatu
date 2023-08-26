'''
Funções relacionadas a uma sentença individual.
'''

import disambiguator_src.word as wd

def nwords(sentence):
    '''
    Retorna o número de palavras da sentença
    '''
    return len(sentence)

def is_ambiguous(sentence):
    '''
    Verifica se uma sentença contém alguma palavra ambígua.
    '''
    return any([wd.is_ambiguous(word) for word in sentence])

def has_tag(sentence, tag):
    '''
    Verifica se a sentença contém alguma palavra com a tag TAG.
    '''
    return any([wd.has_tag(word, tag) for word in sentence])

def tokenize(sentence):
    '''
    Recebe uma sentença na forma de string e retorna um objeto do tipo Sentence.
    '''
    res = []
    
    flag = None
    for w in sentence.split(" "):
        if '/' in w and flag != None:
            res.append(f'{flag} {w}')
            flag = None
        elif not '/' in w:
            flag = w
        else:
            res.append(f'{w}')
    
    tmp = list(zip([i.split("/")[0] for i in res], 
               [i.split("/")[1].split("+") for i in res]))

    res = []
    for i in tmp:
        res.append([i[0], i[1]])
    return res
