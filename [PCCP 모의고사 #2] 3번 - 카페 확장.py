def solution(menu, order, k):
    answer = 0

    def max_people(pairs):
        # 각 시간에 대한 입장과 퇴장 이벤트 생성
        events = []
        for start, end in pairs:
            events.append((start, 1))  # 입장 이벤트
            events.append((end, -1))  # 퇴장 이벤트

        events.sort(key=lambda x: (x[0], x[1]))

        max_count = 0
        current_count = 0
        for t, event in events:
            current_count += event
            # print(t,current_count)
            max_count = max(max_count, current_count)

        return max_count

    people = []
    time = 0
    for i in range(len(order)):
        if time <= k * i:
            time = k * i
        time += menu[order[i]]
        people.append([k * i, time - 1])
    # print(people)
    return max_people(people)
