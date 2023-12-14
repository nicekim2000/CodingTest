from collections import deque

def solution(n, t, m, timetable):
    people=[]
    bus_go = deque([540])
    people_info={}
    for i in range(1,n):
        bus_go.append(540+int(t)*i)

    for time in timetable:
        hour,minute=time.split(":")
        value=int(hour)*60+int(minute)
        people.append(value)
        if value not in people_info:
            people_info[value]=1
        else:
            people_info[value]+=1
    key=list(people_info.keys())
    key.sort()
    people.sort()
    q=deque(key)
    while bus_go:
        cur_bus=bus_go.popleft()
        cur_m=m
        while q and cur_m > 0:
            p=q.popleft()
            if p>cur_bus:
                q.appendleft(p)
                break
            cnt=people_info[p]
            if cnt >=cur_m:
                cnt-=cur_m
                cur_m=0
                people_info[p]=cnt
                if cnt!=0:
                    q.appendleft(p)
                break
            else :
                cur_m-=cnt

    if cur_m > 0 :
        hour=cur_bus//60
        if hour < 10 :
            hour="0"+str(hour)
        else:
            hour=str(hour)
        minute=cur_bus%60
        if minute < 10 :
            minute="0"+str(minute)
        else:
            minute=str(minute)
    else :
        hour=(p-1)//60
        if hour < 10 :
            hour="0"+str(hour)
        else:
            hour=str(hour)
        minute=(p-1)%60
        if minute < 10 :
            minute="0"+str(minute)
        else:
            minute=str(minute)

    return hour + ":" + minute



a=solution(2, 10, 2, ["09:10", "09:09", "08:00"])
