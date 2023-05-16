str1=input()
num_str=''
for _ in str1:
    if _.isdigit():
        num_str+=_
cal=int(num_str)+1
res=[]
while cal//10!=0:
    tmp = cal%10
    res.append(tmp)
    cal=cal//10
res.append(cal)
res.reverse()
output = '[' + ','.join(map(str, res)) + ']'
print(output)
