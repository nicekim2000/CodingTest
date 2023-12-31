
def solution(A, B):
    n=len(A)
    A.sort()
    B.sort()

    cnt=0
    for i in range(n):
        if A[i] >= B[i]:
            find=False
            for j in range(i+1,n):
                if A[i] < B[j]:
                    B[j],B[i]=B[i],B[j]
                    find=True
                    break
            if not find : break
        cnt+=1

    return cnt

a=solution([5,1,3,7]	,[2,2,6,8])
print(a)