def solution(queries):
    answer = []
    child_list = {}
    child_list["RR"] = ["RR", "RR", "RR", "RR"]
    child_list["Rr"] = ["RR", "Rr", "Rr","rr"]
    child_list["rr"] = ["rr", "rr", "rr", "rr"]
    for q in queries:
        line, num = q
        child = []
        for _ in range(line - 1):
            child.append(num % 4)
            if num%4!=0:
                num = (num // 4) + 1
            else:
                num//=4
        child.reverse()
        temp = "Rr"
        for i in range(len(child)):
            temp = child_list[temp][child[i] - 1]
        answer.append(temp)
    return answer

solution([[4,12]])
for i in range(1,65):
    print(i,solution([[4,i]]))