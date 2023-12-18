import sys
import heapq

n=int(input())
time=[]
for _ in range(n):
  s,e=map(int,input().split())
  heapq.heappush(time,(e,s))
cur,_=heapq.heappop(time)
cnt=1
while time:
  end,start=heapq.heappop(time)
  if start >= cur :
    cur=end
    cnt+=1
print(cnt)