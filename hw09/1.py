import time
import datetime

# 获取输入的日期
date_str = input().strip()

# 将日期字符串转换为时间戳
timestamp = time.mktime(time.strptime(date_str, '%Y-%m-%d'))

# 计算下一天的时间戳
one_day = 24 * 60 * 60 # 一天的秒数
next_timestamp = timestamp + one_day

# 计算下一天的年月日
next_date = time.strftime('%Y-%m-%d', time.localtime(next_timestamp))
next_year, next_month, next_day = map(int, next_date.split('-'))

# 判断是否为闰年
if (next_year % 4 == 0 and next_year % 100 != 0) or next_year % 400 == 0: # 闰年
    days_in_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
else: # 平年
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# 调整月份和日期
if next_day > days_in_month[next_month-1]: # 如果日期超过了当月的天数
    next_day = 1
    next_month += 1
if next_month > 12: # 如果月份超过了12
    next_month = 1
    next_year += 1

# 输出结果
print('{:04d}-{:02d}-{:02d}'.format(next_year, next_month, next_day))
