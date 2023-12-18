def solution(n, s):

    a=s//n
    if a==0 : return [-1]
    remain=s-(a*n)
    result=[a for _ in range(n)]
    last=len(result)-1
    for i in range(remain):
        result[last]+=1
        last-=1

    return result

a=solution(4,10)
print(a)