
str=input()
dict={}
for ch in str:
   if ch in dict:
         dict[ch]+=1
   else:
         dict[ch]=1
#输出值最大的键和值
max=0
for key,value in dict.items():
   if value>max:
         max=value
for key,value in dict.items():
   if value==max:
         print(key,value)


