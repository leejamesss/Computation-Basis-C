hash_count={}
while True:
    try:
        n=float(input())
        if n not in hash_count:
            hash_count[n]=1
        else:
            hash_count[n]+=1
    except:
        #双重排序，先按照value排序，再按照key排序
        sorted_items=sorted(hash_count.items(),key=lambda x:(-x[1],x[0]))
        #输出value最大的所有
        for i in sorted_items:
            if i[1]==sorted_items[0][1]:
                print("%.2f"%(i[0]))
            else:
                break
        break
