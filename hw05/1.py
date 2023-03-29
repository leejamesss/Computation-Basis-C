
str=input()
num=0
strcnt=0
other=0
for ch in str:
    if ch.isdigit():
       num+=1
    elif ch.isalpha():
       strcnt+=1
    else:
       other+=1
dict={'字母':strcnt,"数字":num,'其他':other}
print(dict) 
