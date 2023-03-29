
lst=input().split()
dict={}
for ch in lst:
   if ch in dict:
      dict[ch]+=1
   else:
      dict[ch]=1
print(*dict.keys())
