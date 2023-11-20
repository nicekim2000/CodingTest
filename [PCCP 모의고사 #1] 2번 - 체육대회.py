

def solution(ability, number):
    ability.sort()
    a = ability.pop(0)
    b = ability.pop(0)
    temp = a
    a += b
    b += temp

    def swap(arr, n):
        change = False
        for i in range(len(arr)):
            if arr[i] < n:
                change = True
            if arr[i] >= n and change:
                arr[i - 1], n = n, arr[i - 1]
                change = False
                break
        if change:
            arr[-1], n = n, arr[-1]
        return arr, n

    for _ in range(number - 1):
        print([a, b], ability)
        ability, a = swap(ability, a)
        ability, b = swap(ability, b)
        temp = a
        a += b
        b += temp

    print([a, b], ability)
    answer = sum(ability) + a + b
    return answer


solution([1,2,3,4],3)