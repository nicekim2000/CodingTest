def solution(a, b, g, s, w, t):
    answer=4*10**14
    start=0
    end=4*10**14

    while end>=start:
        mid=(start+end)//2
        gold,silver,gs=0,0,0
        for i in range(len(g)):
            move_cnt=mid//t[i]
            if move_cnt%2==1:
                move_cnt=move_cnt//2+1
            else:
                move_cnt=move_cnt//2
            gold+=min(g[i],w[i]*move_cnt)
            silver+=min(s[i],w[i]*move_cnt)
            gs+=min(g[i]+s[i],w[i]*move_cnt)
        if gold >= a and silver >= b and gs >= a+b:
            end=mid-1
            answer=min(answer,mid)
        else:
            start=mid+1
    return answer

a=solution(	90, 500, [70, 70, 0], [0, 0, 500], [100, 100, 2], [4, 8, 1])
print(a)