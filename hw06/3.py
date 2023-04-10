s=[]
while True:
    n=int(input())
    if n==-999:
        break
    s.append(n)
Avg=sum(s)/len(s)
Min=min(s)
Max=max(s)
print("%.2f %.2f %.2f"%(Avg,Max,Min))
