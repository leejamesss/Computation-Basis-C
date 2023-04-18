
def timeshift(s):
    s=s.split(":")
    s=list(map(int,s))
    hour,minute,second=s[0],s[1],s[2]
    time=3600*hour + 60*minute + second
    return time


time_hash={}
while True:
        try:
            city,starttime,endtime=input().split()
            starttime=timeshift(starttime)
            endtime=timeshift(endtime)
            duration=endtime-starttime
            if city in time_hash:
                time_hash[city]=time_hash[city]+duration
            else:
                time_hash[city]=duration
        except:
            break
time_hash=sorted(time_hash.items(),key=lambda x:x[1],reverse=True)
print(time_hash[0][0])

