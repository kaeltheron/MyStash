import datetime

# 计算前一天、前两天、前三天的日期
today = datetime.date.today()
dates = [(today - datetime.timedelta(days=i)).strftime('%y/%m/%Y%m%d') for i in range(1, 4)]

# 读取原文件内容
with open('p.override', 'r') as file:
    content = file.read()

# 使用正则表达式批量替换日期
import re
for i, date in enumerate(dates):
    # 寻找与原文件匹配的日期格式并替换
    content = re.sub(r'\d{2}/\d{2}/\d{8}', date, content, count=1)

# 写回更新后的文件
with open('p.override', 'w') as file:
    file.write(content)
