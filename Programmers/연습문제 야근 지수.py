import heapq
def solution(n, works):
    q = []
    for w in works:
        heapq.heappush(q, -w)
    for _ in range(n):
        if not q: break
        temp = heapq.heappop(q)
        temp += 1
        if temp != 0:
            heapq.heappush(q, temp)
    answer = 0
    for a in q:
        answer += (a ** 2)

    return answer