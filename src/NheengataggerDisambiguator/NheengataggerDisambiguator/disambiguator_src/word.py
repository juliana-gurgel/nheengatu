'''
Funções relacionadas a palavras individuais.
'''
INVALID_TAGS = ["PUNCT", "None", "???"]

def tags(word):
    '''
    Retorna uma lista com as etiquetas de uma palavra.
    '''
    return word[1]

def is_valid(word):
    '''
    Verifica se uma palavra é válida.
    '''
    return not any([t in INVALID_TAGS for t in tags(word)])

def is_ambiguous(word):
    '''
    Verifica se uma palavra é ambígua
    '''
    return len(tags(word)) > 1

def has_tag(word, tag):
    '''
    Verifica se a palavra WORD contém a tag TAG.
    '''
    return tag in tags(word)

def in_ctx_table(word, freq):
    '''
    Verifica se TODAS as etiquetas de WORD se encontram na tabela de contexto FREQ.
    '''
    return all([freq[(freq['tag'] == t)].shape[0] > 0 for t in tags(word)])
