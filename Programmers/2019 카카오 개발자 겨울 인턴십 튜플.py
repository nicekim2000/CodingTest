def solution(s):
    answer = []
    s = s[1:-1]
    op = False
    new_s = []

    for a in s:
        if a == '{':
            op = True
            temp = []
            st = ''
        elif '0' <= a <= '9' and op:
            st += a
        elif a == ',' and op:
            temp.append(int(st))
            st = ''
        elif a == '}':
            temp.append(int(st))
            op = False
            new_s.append(temp)
    new_s.sort(key=lambda x: len(x))
    # print(new_s)
    dic = {}
    for temp in new_s:
        for t in temp:
            if t not in dic:
                dic[t] = True
                answer.append(t)
                break

    return answer