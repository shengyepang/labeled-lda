# -*- coding: utf-8 -*-
import nltk
import nltk.stem
from nltk.tokenize.punkt import PunktSentenceTokenizer, PunktParameters
def read_text(path):
    f=open(path)
    raw=f.read()
    return raw
# def to_sen(raw):
#     sents_tokenizer=nltk.data.load('tokenizers/punkt/english.pickle')
#     sents=sents_tokenizer(raw)
#     return sents
def WordTokener( raw):
    wordsInStr = nltk.word_tokenize(raw)
    return wordsInStr
def cleanWords(wordsInStr):
    cleanWord=[]
    stemWord=[]
    s=nltk.stem.SnowballStemmer('english')
    for word in wordsInStr:
        if word.isdigit():
            del word
    for word in wordsInStr:
        if len(word)==1:
            del word
    for word in wordsInStr:
        cleanWord.append(word.lower())
    for word in cleanWord:
        stemWord.append(s.stem(word))
    return stemWord
if __name__ == '__main__':
    raw=read_text('C:/Users/PSY/Desktop/api_raw.txt')
    print ('1')
    fp = open('C:/Users/PSY/Desktop/raw_result.txt', 'a')
    a_str = ' '.join(map(lambda i: str(i), raw))
    fp.write(a_str)
    fp.close()
    # sent=to_sen(raw)
    words=WordTokener(raw)
    stemWords=cleanWords(words)
    fp = open('C:/Users/PSY/Desktop/result.txt', 'a')
    a_str = ' '.join(map(lambda i: str(i), stemWords))
    fp.write(a_str)
    fp.close()



