# def solution(cap, n, deliveries, pickups):
#     answer = 0
#
#     while True:
#         temp=min(sum(deliveries),cap)
#         target=-1
#         d,p=0,0
#         for i in range(len(deliveries) - 1, -1, -1):
#             if (deliveries[i]!=0 or pickups[i]!=0) and target==-1:
#                 target=i
#             d+=deliveries[i]
#             p+=pickups[i]
#             if d>=cap :
#                 temp=cap
#                 blank=0
#                 break
#             elif p>=cap:
#                 temp=d
#                 blank=cap-d
#                 break
#         blank=cap-temp
#         if target==-1 : break
#         answer+=(target+1)*2
#         for i in range(target,-1,-1):
#             if deliveries[i]!=0 and temp > 0:
#                 if deliveries[i]-temp >= 0 :
#                     deliveries[i]-=temp
#                     blank += temp
#                     temp=0
#                 else:
#                     temp-=deliveries[i]
#                     blank += deliveries[i]
#                     deliveries[i]=0
#             if blank > 0 and pickups[i] > 0 :
#                 if pickups[i]-blank >= 0 :
#                     pickups[i]-=blank
#                     blank=0
#                 else:
#                     blank-=pickups[i]
#                     pickups[i]=0
#
#     return answer


from itertools import zip_longest as zip

def tolist(l):
    n=[]
    for i,d in enumerate(l):
        for _ in range(d):
            n.append(i+1)
    return n

def solution(cap, n, deliveries, pickups):
    d=tolist(deliveries)
    p=tolist(pickups)
    d.reverse()
    p.reverse()
    d=d[::cap]
    p=p[::cap]
    return 2*sum([max(x,y) for x,y in zip(d,p,fillvalue=0)])


a=solution(		4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0])
print(a)