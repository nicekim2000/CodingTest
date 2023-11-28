import heapq
def solution(operations):
    min_q=[]
    cnt=0
    for op in operations:
        o,p=op.split()
        if o=='I':
            heapq.heappush(min_q,int(p))
            cnt+=1
        elif cnt>0:
            if p=='1':
                max_value = max(min_q)
                min_q.remove(max_value)
            else:
                heapq.heappop(min_q)
            cnt-=1
    if cnt==0:
        return [0,0]
    return [max(min_q),heapq.heappop(min_q)]