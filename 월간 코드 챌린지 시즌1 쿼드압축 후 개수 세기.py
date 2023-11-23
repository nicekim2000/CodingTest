def solution(arr):
    global dic
    dic = {}
    dic[0] = 0
    dic[1] = 0
    answer = []

    def check(array):
        temp = array[0][0]
        for i in range(len(array)):
            for j in range(len(array[0])):
                if array[i][j] != temp:
                    return False
        return True

    def dfs(array):
        global dic
        n = len(array) // 2
        region = []
        region.append([x[:n] for x in array[:n]])
        region.append([x[n:] for x in array[:n]])
        region.append([x[:n] for x in array[n:]])
        region.append([x[n:] for x in array[n:]])
        for r in region:
            if check(r):
                dic[r[0][0]] += 1
            else:
                dfs(r)
    if check(arr):
        dic[arr[0][0]]+=1
    else:
        dfs(arr)
    answer.append(dic[0])
    answer.append(dic[1])
    return answer

a=solution([[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]])
print(a)