# 빌런 호석
def change(num,k):
    temp=[]
    while True:
        if num//10==0:
            temp.append(num)
            break
        temp.append(num%10)
        num=num//10
    while len(temp)!=k:
        temp.append(0)
    temp.reverse()
    return temp







# info=[[1,1,1,1,1,1,0],
#       [0,1,1,0,0,0,0],
#       [1,1,0,1,1,0,1],
#       [1,1,1,1,0,0,1],
#       [0,1,1,0,0,1,1],
#       [1,0,1,1,0,1,1],
#       [1,0,1,1,1,1,1],
#       [1,1,1,0,0,0,0],
#       [1,1,1,1,1,1,1],
#       [1,1,1,1,0,1,1]]
#
# convert=[[0 for _ in range(10)]for _ in range(10)]
# for i in range(10):
#     for j in range(i+1,10):
#         value=0
#         for k in range(7):
#             if info[i][k]!=info[j][k]:
#                 value+=1
#         convert[i][j]=value
#         convert[j][i]=value

convert=[[0, 4, 3, 3, 4, 3, 2, 3, 1, 2], [4, 0, 5, 3, 2, 5, 6, 1, 5, 4], [3, 5, 0, 2, 5, 4, 3, 4, 2, 3], [3, 3, 2, 0, 3, 2, 3, 2, 2, 1], [4, 2, 5, 3, 0, 3, 4, 3, 3, 2], [3, 5, 4, 2, 3, 0, 1, 4, 2, 1], [2, 6, 3, 3, 4, 1, 0, 5, 1, 2], [3, 1, 4, 2, 3, 4, 5, 0, 4, 3], [1, 5, 2, 2, 3, 2, 1, 4, 0, 1], [2, 4, 3, 1, 2, 1, 2, 3, 1, 0]]


n,k,p,x=map(int,input().split())
value=0
current=change(x,k)
for i in range(1,n+1):
    if i==x : continue
    answer=change(i,k)
    cnt=0
    for j in range(k):
        a=answer[j]
        b=current[j]
        cnt+=convert[b][a]
    if cnt<=p:

        value+=1

print(value)


