
def solution(A, B):
    A.sort(key=lambda x: x)
    B.sort(key=lambda x: -x)
    num=0
    for i in range(len(A)):
        num+=A[i]*B[i]


    return num


a=solution(	[1, 4, 2], [5, 4, 4])
print(a)