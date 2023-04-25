data = {}
while True:
    line = input().strip()
    if line.lower() == 'quit':
        break
    parts = line.split(',')
    student_id = parts[0]
    score = float(parts[1])
    department = student_id[5:7]
    if department not in data:
        data[department] = {'sum': 0.0, 'count': 0}
    data[department]['sum'] += score
    data[department]['count'] += 1

# 计算平均分数并按照成绩降序排列
avg_scores = []
for department in sorted(data.keys()):
    avg_score = round(data[department]['sum'] / data[department]['count'], 1)
    avg_scores.append((department, avg_score))
avg_scores.sort(key=lambda x: x[1], reverse=True)

# 逐行输出结果
for department, avg_score in avg_scores:
    print('{},{}'.format(department, '{:.1f}'.format(avg_score)))
