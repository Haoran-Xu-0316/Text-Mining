def _write_raw_index(path, text):
    """在csv文件中第一行添加索引字段"""
    with open(path, 'r+', encoding='utf-8') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(text + '\n' + content)

path = 'result.csv'

# 拉出所有日期
import datetime
import random

date_start = '20230401'

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

for i in date_list:
    text = i + ',' + str(random.randint(161, 550))
    _write_raw_index(path, text)
