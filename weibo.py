import pandas as pd

import os
'''
读取文件夹下所有文件的名字并把他们用列表存起来
'''
path = "21.6.5——23.5.1/111"
datanames = os.listdir(path)
print(datanames)

for i in datanames:
    df1 = pd.read_excel("merge1.xlsx")
    file2 = "21.6.5——23.5.1/111/" + i
    df2 = pd.read_excel(file2)

    # 将两个 DataFrame 合并到一个新的 DataFrame 中
    df_merged = pd.concat([df1, df2])

    # 将合并后的 DataFrame 保存到一个新的 Excel 文件中
    df_merged.to_excel("merge1.xlsx", index=False)
