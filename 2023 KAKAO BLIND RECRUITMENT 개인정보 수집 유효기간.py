def solution(today, terms, privacies):
    answer = []
    y, m, d = today.split(".")
    ntoday = int(y) * 12 * 28 + int(m) * 28 + int(d)
    info = {}
    for t in terms:
        a, b = t.split()
        info[a] = int(b) * 28
    n = 1
    for p in privacies:
        date, a = p.split()
        dy, dm, dd = date.split(".")
        num = int(dy) * 12 * 28 + int(dm) * 28 + int(dd) + info[a]

        if num <= ntoday:
            answer.append(n)
        n += 1
    return answer