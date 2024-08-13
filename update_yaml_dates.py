import datetime
import re

# 计算T-1、T-2、T-3的日期
today = datetime.date.today()
dates_to_use = [(today - datetime.timedelta(days=i)).strftime('%Y/%m/%Y%m%d') for i in range(1, 4)]  # T-1, T-2, T-3

# 读取原文件内容
with open('p.override', 'r') as file:
    content = file.read()

# 正则表达式匹配所有日期，确保匹配格式为yyyy/mm/yyyymmdd
date_pattern = r'\d{4}/\d{2}/\d{8}'

# 找到所有匹配的日期
found_dates = re.findall(date_pattern, content)

# 如果找到的日期数量少于3个，无法为每个T-i找到对应的日期
if len(found_dates) < 3:
    print("文件中的日期数量不足以替换T-1, T-2, T-3。")
else:
    # 替换所有找到的日期为T-1, T-2, T-3
    for i, original_date in enumerate(found_dates, start=1):
        # 替换日期，这里假设替换顺序是按照文件中出现的顺序
        content = re.sub(r'\b' + re.escape(original_date) + r'\b', dates_to_use[i-1], content)

# 写回更新后的文件
with open('p.override', 'w') as file:
    file.write(content)