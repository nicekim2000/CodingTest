# 다른 부모를 섬기고 있었는데 부모가 변할경우 부모리스트의 전체적인 업데이트가 필요함
def solution(n, wires):
    def find_par(n, par):
        if par[n] == n:
            return n
        else:
            return find_par(par[n], par)

    def change(par, x, y):
        for i in range(len(par)):
            if par[i] == x:
                par[i] = y
        return par

    answer = n + 1
    wires.sort()
    print(wires)
    for i in range(n):
        temp = wires[:i] + wires[i + 1:]
        par = [x for x in range(n + 1)]
        for t in temp:
            a = find_par(t[0], par)
            b = find_par(t[1], par)
            if a < b:
                par = change(par, b, a)
                par[t[1]] = a
            else:
                par = change(par, a, b)
                par[t[0]]=b
        print(par)
        temp_num = par[1]
        cnt1, cnt2 = 1, 0
        for p in range(2, len(par)):
            if temp_num != par[p]:
                cnt2 += 1
            else:
                cnt1 += 1
        answer = min(answer, abs(cnt2 - cnt1))
    return answer


a = solution(6,  [[1, 4], [6, 3], [2, 5], [5, 1], [5, 3]])
print(a)
