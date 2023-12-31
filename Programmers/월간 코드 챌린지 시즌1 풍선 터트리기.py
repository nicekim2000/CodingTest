
answer=set()
def bomb(a,cheat):
    global answer
    if len(a)==1:
        answer.add(a[0])
    for i in range(len(a)-1):
        x,y=a[i],a[i+1]
        # print(a)
        # print(x,y)
        # print(a[:i]+a[i+2:])
        # print()
        if not cheat:
            bomb(a[:i]+a[i+2:]+[min(x,y)],1)
        bomb(a[:i]+a[i+2:]+[max(x,y)],cheat)

def solution(a):
    bomb(a,0)
    print(answer)
    return len(answer)


a=solution(	[-16, 27, 65, -2, 58, -92, -71, -68, -61, -33])
print(a)