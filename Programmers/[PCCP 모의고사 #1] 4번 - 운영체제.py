import heapq
def solution(program):
    answer = [0] * 11
    program = sorted(program, key=lambda x: x[1])
    q = []
    running = 0

    while q or program:
        if not q:
            running=program[0][1]
            while program and program[0][1] <= running:
                pri, start, time = program.pop(0)
                heapq.heappush(q, (pri, start, time))
        temp_p, temp_s, temp_t = heapq.heappop(q)
        if temp_s > running :
            running=temp_s
        answer[temp_p] += running - temp_s
        running += temp_t
        while program and program[0][1] <= running:
            pri, start, time = program.pop(0)
            heapq.heappush(q, (pri, start, time))
    answer[0] = running

    print(answer)
    return answer

solution(  [[2, 0, 3], [1, 3, 2], [3, 2, 1], [3, 4, 2]]
)
