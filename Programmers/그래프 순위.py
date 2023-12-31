from collections import deque


def solution(n, results):
    answer = 0
    uprank = [[] for _ in range(n + 1)]
    downrank = [[] for _ in range(n + 1)]
    for result in results:
        winner, loser = result
        uprank[loser].append(winner)
        downrank[winner].append(loser)
    for i in range(1, n + 1):
        us = set()
        ds = set()
        uq = deque(uprank[i])
        dq = deque(downrank[i])
        while uq:
            temp_up = uq.popleft()
            if temp_up in us: continue
            us.add(temp_up)
            for t in uprank[temp_up]:
                uq.append(t)
        while dq:
            temp_down = dq.popleft()
            if temp_down in ds: continue
            ds.add(temp_down)
            for t in downrank[temp_down]:
                dq.append(t)
        if len(us) + len(ds) == n - 1:
            answer += 1

    return answer