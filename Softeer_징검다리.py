import sys

n=int(input())
info=list(map(int,input().split()))
ss=[1 for _ in range(n)]
for i in range(n):
  temp=info[i]
  for j in range(i):
    if info[i]>info[j]:
      ss[i]=max(ss[i],ss[j]+1)
print(max(ss))