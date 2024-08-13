import datetime
import re

# 计算T-1、T-2、T-3的日期
today = datetime.date.today()
date_to_replace = today.strftime('%Y/%m/%d')  # 今天的日期，用于格式化
dates_to_use = [(today - datetime.timedelta(days=i)).strftime('%Y/%m/%d') for i in range(1, 4)]  # T-1, T-2, T-3

# 读取原文件内容
with open('p.override', 'r') as file:
    content = file.read()

# 正则表达式匹配所有日期
date_pattern = r'\d{4}/\d{2}/\d{8}'

# 创建一个字典，用于存储所有找到的日期及其对应的替换日期
dates_dict = {match: dates_to_use.pop(0) for match in re.findall(date_pattern, content)}

# 替换所有找到的日期
for original_date, new_date in dates_dict.items():
    content = re.sub(r'\b' + re.escape(original_date) + r'\b', new_date, content)

# 写回更新后的文件
with open('p.override', 'w') as file:
    file.write(content)