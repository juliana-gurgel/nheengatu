import logging
from .utils import *
import disambiguator_src.word as wd
import disambiguator_src.sentence as st


def disambiguate_sentence(s, freq):
    logger = logging.getLogger('sentence')
    
    sentence = st.tokenize(s)

    logger.info(f'Sentença {sentence}')

    # Condições para não resolver ambiguidade
    if ((not st.is_ambiguous(sentence)) or (st.nwords(sentence) == 1)):
        logger.info(f' A sentença não contém ambiguidades!')
        logger.info(f' Sentença desambiguada: {str(sentence)}')
        return s
    else:
        for i in range(st.nwords(sentence)):
            #word_curr, tag_curr = sentence[i]
            word = sentence[i]
            if wd.is_ambiguous(word) and wd.is_valid(word):
                logger.warning(f' > Palavra {word[0]} é ambígua ({word})')
                if wd.in_ctx_table(word, freq):
                    flag = [wd.tags(word), 0.0]
                    for t in wd.tags(word):
                        logger.info(f'  > tag {t}')
                        media = 0
                        # Início da sentença
                        if i == 0:
                            word_next = sentence[i+1]
                            if (not wd.is_ambiguous(word_next)) and wd.is_valid(word_next):
                                qry = "+".join(wd.tags(word_next))
                                res_next = freq[(freq['tag'] == t) & (freq['prev_next'] == 'next') & (freq['pos_tag'] == qry)]
                                if res_next.shape[0] > 0:
                                    media = res_next[['frequency']].iat[0,0]
                                #if media > flag[1]:
                                #    flag = [t, media]
                        # Final da sentença
                        elif i == (len(sentence) - 1):
                            word_prev = sentence[i-1]
                            if (not wd.is_ambiguous(word_prev)) and wd.is_valid(word_prev):
                                #word_prev, tag_prev = sentence[i-1]
                                qry = "+".join(wd.tags(word_prev))
                                res_prev = freq[(freq['tag'] == t) & (freq['prev_next'] == 'prev') & (freq['pos_tag'] == qry)]
                                if res_prev.shape[0] > 0:
                                    media = res_prev[['frequency']].iat[0,0]
                        # Meio da sentenca
                        else:
                            word_prev = sentence[i-1]
                            word_next = sentence[i+1]
                            if (not wd.is_ambiguous(word_next)) and wd.is_valid(word_next):
                                #word_next, tag_next = sentence[i+1]
                                qry = "+".join(wd.tags(word_next))
                                res_next = freq[(freq['tag'] == t) & (freq['prev_next'] == 'next') & (freq['pos_tag'] == qry)]
                                if res_next.shape[0] > 0:
                                    media = res_next[['frequency']].iat[0,0]
                            if (not wd.is_ambiguous(word_prev)) and wd.is_valid(word_prev):
                                qry = "+".join(wd.tags(word_prev))
                                res_prev = freq[(freq['tag'] == t) & (freq['prev_next'] == 'prev') & (freq['pos_tag'] == qry)]
                                if res_prev.shape[0] > 0:
                                    media = res_prev[['frequency']].iat[0,0]
                        if media > flag[1]:
                            flag = [t, media]
                    sentence[i][1] = [flag[0]] if isinstance(flag[0], str) else flag[0]
        return " ".join([f'{w[0]}/{"+".join(w[1])}' for w in sentence])
        
        
def disambiguate_corpus(corpus, freq):
    logger = logging.getLogger('corpus')

    #res = []
    count_file, total, fail, passed = 1, len(corpus), 0, 0
    for fname, fcontents in corpus.items():
        sentences = fcontents.split('\n')
        logger.info(f' [{count_file}/{total}] Desambiguando arquivo {fname} ({len(sentences)} sentenças)')     
        
        count_sentence = 1
        for sentence in sentences:
            try:
                logger.info(f' [{count_sentence}/{len(sentences)}] Sentença {sentence}')
                #res.append(str(disambiguate_sentence(sentence, freq)))
                s = str(disambiguate_sentence(sentence, freq))
                #logger.info(f'{s}')
                #logger.info(f'=> Sentença desambiguada: {str(s)}\n')
                passed += 1
                count_sentence += 1
            except:
                logger.error(f'Arquivo {fname} deu problema!')
                fail += 1
                count_sentence += 1 
    logger.info(f'Sentenças concluídas: {passed}')
    logger.info(f'Sentenças com falha: {fail}')

