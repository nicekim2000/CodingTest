def solution(begin, target, words):
    def compare(a, b):
        cnt = 0
        for i in range(len(a)):
            if a[i] != b[i]:
                cnt += 1
        if cnt == 1: return True
        return False

    def dfs(s, t, ws, cnt):
        if s==t : return cnt
        value = 51
        for i in range(len(ws)):
            if compare(s, ws[i]):
                temp = ws[:i] + ws[i + 1:]
                value = min(dfs(ws[i], t, temp, cnt + 1), value)
        return value
    answer=dfs(begin, target, words, 0)
    if answer==51 : return 0
    return answer

a=solution(	"hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])
print(a)