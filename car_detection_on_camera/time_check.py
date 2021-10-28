import datetime
from time import sleep

def get_second(t):
    h = int(t.split(":")[0])*3600
    m = int(t.split(":")[1])*60
    return h+m

starttime = "7:00"
endtime = "17:00"
now = datetime.datetime.now()
nowtime = now.strftime("%H:%M")
start = get_second(starttime)
end = get_second(endtime)
now = get_second(nowtime)
print(start,end,now)
if not (start < now and end > now):
    while True:
        print("wait")
        sleep(60*60)
        
    
    


