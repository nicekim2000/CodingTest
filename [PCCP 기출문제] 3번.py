import math
def solution(h1, m1, s1, h2, m2, s2):
    time1=h1*60*60+m1*60+s1
    time2=h2*60*60+m2*60+s2
    sec=time2-time1
    h,m,s=((h1*5)+(1/12)*m1+(1/43200)*s1)%60,m1+(1/43200)*s1,s1
    temp_h,temp_m=h,m
    up_h,up_m=0,0
    print(h,m,s)
    h_count=(m1%12)*60+s1
    m_count=s1
    if h==s and m==s : count=1
    else : count=0
    for i in range(1,sec+1):


        s=(s+1)%60

        if (i+m_count)%60==0:

            m=(math.ceil(m))%60
        else:
            m = (m + float(1 / 60)) % 60
        if (i+h_count)%720==0:
            print(h, m, s)
            h=(math.ceil(h))%60
            print(h, m, s)
        else:
            h = (h + float(1 / 43200)) % 60

        if (s-1)%60 < temp_m < s :
            count+=1
        if (s-1)%60 < temp_h < s and h!=m:
            count+=1

        #
        # up_h=(math.ceil(temp_h))%60
        # up_m=(math.ceil(temp_m))%60
        # if up_h==s :
        #     count+=1
        #     yes=True
        #     # print("find")
        #     # print(h, m, s)
        #     # print(up_h, up_m)
        # if up_m==s and h!=m :
        #     count+=1
        #     # print("find")
        #     # print(h, m, s)
        #     # print(up_h, up_m)
        temp_h=h
        temp_m=m


    return count

solution(				0, 0, 0, 23, 59, 59)