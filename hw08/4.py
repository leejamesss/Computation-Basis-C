import re

text = input().strip()
# 将非英文字母换成空格
text = re.sub(r'[^a-zA-Z]', ' ', text)
# 分割为单词列表
words = text.split()
# 统计单词数量
count = len(words)
print(count)
