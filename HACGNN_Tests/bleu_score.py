from traceback import print_tb
from nltk.translate.bleu_score import sentence_bleu
import re

predictions = []
with open('C:\\Users\\dmasrour\\Documents\\HAConvGNN\\modelout\\predictions\\predict_notebook.txt', 'r') as p:
    for sentence in p:
        if '<s>' in sentence and '</s>' in sentence:
            m = re.search('<s>(.+?)</s>', sentence).group(1)
            predictions.append(m.split())
        elif '<s>' in sentence and  '</s>' not in sentence:
            m = re.search('<s>(.+?)', sentence).group(1)
            predictions.append(m.split())
        elif '</s>' in sentence and  '<s>' not in sentence:
            m = re.search('(.+?)</s>', sentence).group(1)
            predictions.append(m.split())
    print(type(predictions))


expected = []
with open('C:\\Users\\dmasrour\\Documents\\HAConvGNN\\final_data\\coms.test', 'r') as p:
    i = 0
    for sentence in p:
        i += 1
        if i == 59: break
        if '<s>' in sentence and '</s>' in sentence:
            m = re.search('<s>(.+?)</s>', sentence).group(1)
            expected.append(m.split())
        elif '<s>' in sentence and  '</s>' not in sentence:
            m = re.search('<s>(.+?)', sentence).group(1)
            expected.append(m.split())
        elif '</s>' in sentence and  '<s>' not in sentence:
            m = re.search('(.+?)</s>', sentence).group(1)
            expected.append(m.split())
    print(type(expected))



for pred in predictions:
    bleu_score = sentence_bleu(expected, pred)
    print(bleu_score)