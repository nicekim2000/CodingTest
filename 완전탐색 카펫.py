def solution(brown, yellow):
    answer = []
    s=(brown-4)//2
    m=yellow
    cnt=1
    while True:
        if m%cnt==0:
            temp=m//cnt
            if temp+cnt==s:
                answer=[temp+2,cnt+2]
                answer.sort(key=lambda x: -x)
                return answer
        cnt+=1
    return answer