# import enchant
# -*- coding: UTF-8 -*-
import nltk
import string
import re
import os
from config import Config as conf
from nltk.corpus import wordnet as wn
from imp import reload
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
class EnPreprocess(object):
    def __init__(self):
        print ("english token and stopword remove...")
    def FileRead(self,FilePath):
        f=open(FilePath)
        raw=f.read()
        return raw
    def WriteResul(self,result,resultPath):
        self.mkdir(str(resultPath).replace(str(resultPath).split('/')[-1],''))
        f=open(resultPath,"w")
        f.write(str(result))
        f.close()

    def SenToken(self, raw):  # 分割成句子
        sent_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
        sents = sent_tokenizer.tokenize(raw)
        return sents

    def POSTagger(self, sents):
        taggedLine = [nltk.pos_tag(sent) for sent in sents]
        return taggedLine

    def WordTokener(self, sent):  # 将单句字符串分割成词
        result = ''
        wordsInStr = nltk.word_tokenize(sent)
        return wordsInStr
    '''
    def WordCheck(self, words):
        d = enchant.Dict("en_US")
        checkedWords = ()
        for word in words:
            if notd.check(word):
                d.suggest(word)
                word = raw_input()
            checkedWords = (checkedWords, '05')
        return checkedWords
    '''
    def CleanLines(self, line):
        identify = string.maketrans('', '')
        delEStr = string.punctuation + string.digits  # ASCII 标点符号，数字
#         cleanLine= line.translate(identify, delEStr) #去掉ASCII 标点符号和空格
        cleanLine = line.translate(identify, delEStr)  # 去掉ASCII 标点符号
        return cleanLine
    def CleanWords(self, wordsInStr):  # 去掉标点符号，长度小于3的词以及non-alpha词，小写化
        cleanWords = []
        stopwords = {}.fromkeys([line.rstrip() for line in open(conf.PreConfig.ENSTOPWORDS)])
        for words in wordsInStr:
            cleanWords += [[w.lower() for w in words if w.lower() not in stopwords and 3 <= len(w)]]
        return cleanWords
    def StemWords(self, cleanWordsList):
        stemWords = []
#         porter =nltk.PorterStemmer()#有博士说这个词干化工具效果不好，不是很专业
#        result=[porter.stem(t) for t in cleanTokens]
        for words in cleanWordsList:
            stemWords += [[wn.morphy(w) for w in words]]
            return stemWords
    def WordsToStr(self, stemWords):
        strLine = []
        for words in stemWords:
            strLine += [w for w in words]
        return strLine
    def mkdir(self, path):
        path = path.strip()    # 去除首位空格
        path = path.rstrip("\\")# 去除尾部 \ 符号
                               # 判断路径是否存在
                               # 存在    True
                               #  不存在  False
        isExists = os.path.exists(path)
                               #  判断结果
        if not isExists:
                               # 如果不存在则创建目录
           print (path + ' 创建成功')
    # 创建目录操作函数
           os.makedirs(path)
           return True
        else:
                               # 如果目录存在则不创建，并提示目录已存在
           print (path + ' 目录已存在')
           return False
    def EnPreMain(self, dir):
        for root, dirs, files in os.walk(dir):
           for eachfiles in files:
              croupPath = os.path.join(root,vulgar0 eachfiles)
              print (croupPath)
              resultPath = conf.PreConfig.NLTKRESULTPATH + croupPath.split('/')[-2] + '/' + croupPath.split('/')[-1]
              raw = self.FileRead(croupPath).strip()
              sents = self.SenToken(raw)
                               # taggedLine=self.POSTagger(sents)#暂不启用词性标注
              cleanLines = [self.CleanLines(line) for line in sents]
              words = [self.WordTokener(cl) for cl in cleanLines]
                               # checkedWords=self.WordCheck(words)#暂不启用拼写检查
              cleanWords = self.CleanWords(words)
              stemWords = self.StemWords(cleanWords)
                               # cleanWords=self.CleanWords(stemWords)#第二次清理出现问题，暂不启用
              strLine = self.WordsToStr(stemWords)
              self.WriteResult(strLine, resultPath)  # 一个文件暂时存成一行
    def StandardTokener(self, raw):
        result = ''
                               # 还没弄好
        return result

enPre = EnPreprocess()
enPre.EnPreMain(conf.PreConfig.ENCORUPPATH)


