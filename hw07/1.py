s=list(map(int,input().split(",")))
missing=0
duplicate=0
for i in range(len(s)):
    if s.count(i+1)==0:
        missing=i+1
    if s.count(i+1)==2:
        duplicate=i+1
print([duplicate,missing])
