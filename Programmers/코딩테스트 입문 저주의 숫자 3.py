def solution(n):
    answer = 0

    def find(num):
        if num % 3 == 0: return True
        while num > 10:
            remain = num % 10
            if remain == 3: return True
            num = num // 10
        if num == 3: return True
        return False

    for _ in range(1, n + 1):
        answer += 1
        while find(answer):
            answer+=1
    return answer

a=solution(40)
print(a)