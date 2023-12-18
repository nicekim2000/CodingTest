def solution(n, t, m, p):
    def convert(num,form):
        a=num//form
        b=num%form
        result=''
        if a<form:
            if a!=0:
                return result+dic_list[b]+dic_list[a]
            else:
                return result+dic_list[b]
        else:
            result+=dic_list[b]
            return result+convert(a,form)
    dic_list=[str(x) for x in range(10)]
    alpha=['A','B','C','D','E','F']
    dic_list+=alpha


    answer = ''
    num=0
    cnt=0
    result=''
    while True:
        temp=convert(num,n)
        temp=temp[::-1]
        cnt+=len(temp)
        result+=temp
        if cnt>=t*m: break
        num+=1
    for i in range(t):
        answer+=result[i*m+(p-1)]
    return answer

a=solution(		16, 16, 2, 2)
print(a)