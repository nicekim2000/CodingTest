def solution(bandage, health, attacks):
    answer = health

    def info(prev_attack, answer, time, damage):
        period = time - prev_attack
        success = period // bandage[0]
        answer += (period * bandage[1] + success * bandage[2])
        if answer >= health:
            answer = health
        prev_attack = time + 1
        answer -= damage
        return prev_attack, answer

    prev_attack = 0
    for att in attacks:
        prev_attack, answer = info(prev_attack, answer, att[0] - 1, att[1])
        # print(prev_attack,answer)
        if answer < 1:
            return -1
    return answer

