import xlrd

file_path = 'merge1.xlsx'
data = xlrd.open_workbook(file_path)
table = data.sheet_by_name('Sheet1')

lst = []

# 获取总行数
nrows = table.nrows

print(nrows)

date = '20210605'
count = 0

for i in range(1, nrows):
    # 获取一个单元格的数值，例如第5行第6列
    cell_value = table.cell(i, 9).value
    value = cell_value[0:4] + cell_value[5:7] + cell_value[8:10]
    if value == date:
        count += 1
    else:
        l = [date, count]
        lst.append(l)
        date = value
        count = 0
print(lst)

lst1 = []
record = []
date = '202106'
for i in lst:
    if i[0][0:6] == date:
        record.append(i[1])
    else:

        mx = max(record)
        mn = min(record)
        l = [date, mn, mx]
        lst1.append(l)
        date = i[0][0:6]
        record = []

print(lst1)

# 拉出所有日期
import datetime
import random

date_start = '20210605'

date_end = '20230430'

date_start = datetime.datetime.strptime(date_start, '%Y%m%d')

date_end = datetime.datetime.strptime(date_end, '%Y%m%d')

date_list = []

date_list.append(date_start.strftime('%Y%m%d'))

while date_start < date_end:

    date_start += datetime.timedelta(days=+1)  # 日期加一天

    date_list.append(date_start.strftime('%Y%m%d'))  # 日期存入列表

print(date_list)
# 拉出结束

lst2 = []
for i in date_list:
    for j in lst1:
        if j[0] == i[0:6]:
            lst2.append([i, random.randint(j[1], j[2])])
for i in range(len(lst2)):
    for j in lst:
        if j[0] == lst2[i][0]:
            lst2[i] = j
print(lst2)


def _write_raw_index(path, text):
    """在csv文件中第一行添加索引字段"""
    with open(path, 'r+', encoding='utf-8') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(text + '\n' + content)

path = 'result.csv'

for i in lst2:
    text = i[0]+','+str(i[1])
    _write_raw_index(path, text)

