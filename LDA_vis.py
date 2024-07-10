import gensim
from gensim import corpora
import matplotlib.pyplot as plt
import jieba
import matplotlib
import numpy as np
from gensim.models.coherencemodel import CoherenceModel
from gensim.models.ldamodel import LdaModel
import pandas as pd
import os
import pyLDAvis.gensim

data = []
with open("fenci.txt", "r", encoding='utf-8') as f:
    data = f.readlines()

for i in range(len(data)):
    data[i] = data[i][0:-1]
data = data + ['你', '我', '的', '了', '在', '吧', '吃', '是', '也', '都', '不', '就', '我们', '还', '大家',
                                 '你们', '就是', '很', '有', '和', '说', '一个',  '真的', '里面', '这个', '但是',
                                 '上', '还是', '去', '来', '去', '还有', '这', '不过', '比较', '什么', '又', '有点', '时候',
                                 '中', '才', '到', '但', '其他', '因为', '其它', '薄荷', '里', '外', '如果', '那', '这', '不是',
                                 '怎么', '可能', '最后', '而且', '一样',  '然后', '所以', '这家', '店', '没',
                                 '现在', '给', '很多', '没', '的话', '完', '这里', '那里', '想', '人', '一份', '啊',
                                 '啊', '那个', '对', '过', '太', '之前', '哦', '应该', '呢', '跟', '再', '在', '个人', '看', '等',
                                 '会', '过来', '过去', '已经', '觉得', '大', '下次', '上次', '基本', '啦', '哈', '知道', '之后', '那种',
                                 '让', '把', '做', '东西', '总体', '能', '不能', '不会', '呀', '并', '走', '哦', '大', '小', '点',
                                 '多', '要', '个', '店里', '其实', '感觉', '一家', '一下', '看到', '蛮',
                                 '两个', '用', '今天', '虽然', '一些', '最', '这么', '家', '蛋', '找', '意', '奥', '奥利', '问', '菜', '换']

filePath = 'E:\dazhongdianping-master\qs'
lst = os.listdir(filePath)
data_set = []

for i in range(len(lst)):
    # 读取文件
    pd_data = pd.read_csv(filePath+'\\'+str(lst[i]), encoding='GBK')

    # 读取内容
    text = pd_data['评论'].tolist()
    file_object2 = []

    # 切割分词
    for i in text:
        wordlist = jieba.cut(i)
        result = ' '.join(wordlist)
        file_object2.append(result)

    # 放进一个二级列表中，每个列表代表一个评论
    for i in range(len(file_object2)):
        result = []
        seg_list = file_object2[i].split()
        for w in seg_list:   # 读取每一行分词
            if w not in data:
                result.append(w)
        data_set.append(result)


dictionary = corpora.Dictionary(data_set)  # 构建词典
corpus = [dictionary.doc2bow(text) for text in data_set]   # 表示为第几个单词出现了几次

lda = LdaModel(corpus=corpus, id2word=dictionary, num_topics=15, passes=30, random_state=1)
topic_list = lda.print_topics()
print(topic_list)

# for i in lda.get_document_topics(corpus)[:]:
#     listj = []
#     for j in i:
#         listj.append(j[1])
#     bz = listj.index(max(listj))
#     print(i[bz][0])

data = pyLDAvis.gensim.prepare(lda, corpus, dictionary)
print(data)
term = data[1]['Term'].tolist()
Freq = data[1]['Total'].tolist()
print(term)
print(Freq)
pyLDAvis.save_html(data, '5topic.html')

