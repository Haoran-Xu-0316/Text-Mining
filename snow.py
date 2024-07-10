import snownlp
import matplotlib
import pandas as pd
from pandas import DataFrame
import xlrd
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from pyecharts import options as opts
from pyecharts.charts import Pie
from palettable.colorbrewer.qualitative import Pastel1_7
import os


plt.rcParams['font.sans-serif'] = 'simhei'
plt.rcParams['axes.unicode_minus']=False

data = []
with open("fenci.txt", "r", encoding='utf-8') as f:
    data = f.readlines()

for i in range(len(data)):
    data[i] = data[i][0:-1]
data = data + ['你', '我', '的', '了', '在', '吧', '吃', '是', '也', '都', '不', '好', '就', '我们', '还', '大家',
                                 '你们', '就是', '很', '有', '和', '说', '一个', '不错', '可以', '没有', '真的', '里面', '这个', '但是',
                                 '上', '还是', '去', '来', '去', '还有', '这', '一般', '不过', '比较', '什么', '又', '有点', '时候',
                                 '中', '才', '到', '但', '挺', '其他', '因为', '其它', '薄荷', '里', '外', '如果', '那', '这', '不是',
                                 '怎么', '可能', '最后', '而且', '一样', '一般', '然后', '所以', '这家', '店', '非常', '没',
                                 '现在', '给', '很多', '没', '的话', '完', '这里', '那里', '想', '人', '一份', '特别', '啊',
                                 '啊', '一点', '那个', '对', '过', '太', '之前', '哦', '应该', '呢', '跟', '再', '在', '个人', '看', '等',
                                 '会', '过来', '过去', '已经', '觉得', '大', '一点', '下次', '上次', '基本', '啦', '哈', '知道', '之后', '那种',
                                 '让', '把', '哈哈哈', '做', '东西', '总体', '能', '不能', '不会', '呀', '并', '走', '哦', '大', '小', '点',
                                 '多', '喜欢', '要', '个', '店里', '其实', '感觉', '一家', '一下', '看到', '好吃', '蛮', '超级',
                                 '量', '两个', '用', '今天', '虽然', '一些', '最', '这么', '家', '蛋', '找', '意', '奥', '奥利', '问', '换', '催']

filePath = 'E:\dazhongdianping-master\qs'
lst = os.listdir(filePath)
# 读取文件
pd_data = pd.read_csv(filePath+'\\'+str(lst[0]), encoding='GBK')
filelist = []
for i in lst:
    pd_data = pd.read_csv(filePath + '\\' + i, encoding='GBK')
    text = pd_data['评论'].tolist()
    filelist.append(text)

positive = 0
negative = 0
neutral = 0
for i in filelist:
    for j in i:
        x = snownlp.SnowNLP(j).sentiments
        if (x >= 0.45 and x <= 0.55):
            neutral += 1
        if x > 0.55:
            positive += 1
        if x < 0.45:
            negative += 1
# print(正向评论_positive)
# print(负向评论_negative)
# print(中性评论_neutral)

x = ['正向评论', '负向评论', '中性评论']
y = [positive, negative, neutral]
plt.pie(y, pctdistance=0.85, autopct='%.1f%%', labels=x, colors=Pastel1_7.hex_colors, wedgeprops=dict(width=0.3, edgecolor='w'))
plt.legend(x, loc='upper left')
plt.title('--情感分类环形图')
plt.show()