import os
import jieba
import jieba.analyse as analyse
import pandas as pd
from stylecloud import gen_stylecloud

filePath = 'E:\dazhongdianping-master\qs'
lst = os.listdir(filePath)
print(lst)

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

'''# 读取文件
pd_data = pd.read_csv(filePath+'\\'+str(lst[0]), encoding='GBK')

# 读取内容
text = pd_data['评论'].tolist()

# 切割分词
wordlist = jieba.cut(''.join(text))
result = ' '.join(wordlist)'''

result = ''

for i in lst:
    pd_data = pd.read_csv(filePath + '\\' + i, encoding='GBK')
    text = pd_data['评论'].tolist()
    try:
        wordlist = jieba.cut(''.join(text))
    except:
        print(i)
    res = ' '.join(wordlist)
    result = result + ' ' + res

gen_stylecloud(text=result,
               icon_name='fas fa-apple-alt',
               palette='cartocolors.sequential.BluGrn_7',
               font_path='msyh.ttc',
               background_color='white',
               output_name='666.jpg',
               max_font_size=100,
               max_words=100,
               custom_stopwords=data
               )
print("运行成功")
