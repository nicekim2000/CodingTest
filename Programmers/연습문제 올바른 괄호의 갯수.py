answer = 0
def dfs(n,cur):
    global answer
    if cur < 0 : return
    if n==0 and cur==0 :
        answer+=1
    if n>0:
        dfs(n-1,cur+1)
    dfs(n,cur-1)

def solution(n):
    dfs(n,0)
    return answer

a=solution(3)
print(a)