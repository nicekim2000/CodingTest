import sys
input=sys.stdin.readline

n,k=map(int,input().split())
score=list(map(int,input().split()))
stack=[0 for _ in range(n+1)]
for i in range(1,n+1):
  stack[i]=stack[i-1]+score[i-1]
for _ in range(k):
  a,b=map(int,input().split())
  result=round((stack[b]-stack[a-1])/(b-a+1),2)
  print("{:.2f}".format(result))