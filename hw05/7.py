
n=int(input())
lst=input().split(",")
birthlst=[]
for i in range(n):
    id=input()
    birthlst.append(int(id[10:12]))
for j in lst:
    cnt=birthlst.count(int(j))
    if cnt==0:
        print("活动取消")
    elif 1<=cnt and cnt<=5:
        print("静园草坪")
    elif 6<=cnt and cnt<=10:
        print("百讲")
    else:
        print("邱德拔")

        

