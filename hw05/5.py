begin=input().split(":")
end=input().split(":")
preRecord=7*60
afterRecord=23*60
Mid=12*60
beginTime=int(begin[0])*60+int(begin[1])
endTime=int(end[0])*60+int(end[1])
reduce=0
def time(beginTime,endTime,reduce):

      if beginTime<Mid and endTime>Mid:
         reduce=reduce+30
      if beginTime<preRecord:
         beginTime=preRecord
      if endTime>afterRecord:
         endTime=afterRecord
      total=endTime-beginTime-reduce
      hour=(endTime-beginTime-reduce)//60
      min=(endTime-beginTime-reduce)%60
      if total<0:
         print("0小时")
      else:
         print("%d小时%d分钟"%(hour,min))
time(beginTime,endTime,reduce)



