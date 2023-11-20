# 스카이라인 쉬운거

n=int(input())
stack=[]
value=0
cnt=0
for _ in range(n):
    _,temp=map(int,input().split())
    while stack:
        s=stack.pop()
        if s<temp:
            stack.append(s)
            break
        elif s>temp:
            cnt+=1
    if temp!=0:
        stack.append(temp)
cnt+=len(stack)
print(cnt)
