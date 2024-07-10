import datetime


date_start = '20180501'


date_end = '20210430'

date_start = datetime.datetime.strptime(date_start, '%Y%m%d')

date_end = datetime.datetime.strptime(date_end, '%Y%m%d')

date_list = []

date_list.append(date_start.strftime('%Y%m%d'))

while date_start < date_end:

    date_start += datetime.timedelta(days=+1)  # 日期加一天

    date_list.append(date_start.strftime('%Y%m%d'))  # 日期存入列表

print(date_list)