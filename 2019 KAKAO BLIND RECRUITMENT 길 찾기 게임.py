import sys
sys.setrecursionlimit(10**6)
# 6번,7번 런타임 에러 <- 재귀 최대 1000번인데 노드가 100000개라 늘려줘야함
def solution(nodeinfo):
    global later,pre
    later=[]
    pre=[]
    def make_tree(arr,root_x):
        global later,pre
        if not arr :
            return
        if len(arr)==1 :
            pre.append(arr[0][2])
            later.append(arr[0][2])
            return
        temp_y=arr[0][1]
        root_list=[]
        for i in range(len(arr)):
            if arr[i][1]==temp_y:
                root_list.append(arr[i])
            else:
                nodeinfo=arr[i:]
                break

        if len(root_list)==1:
            l,r=[],[]
            c_x=root_list[0][0]
            for i in range(len(nodeinfo)):
                if nodeinfo[i][0] < c_x:
                    l.append(nodeinfo[i])
                else:
                    r.append(nodeinfo[i])
            pre.append(root_list[0][2])
            make_tree(l,c_x)
            make_tree(r,c_x)
            later.append(root_list[0][2])
            return

    cnt=1
    answer = []
    for i in range(len(nodeinfo)):
        nodeinfo[i].append(cnt)
        cnt+=1
    nodeinfo.sort(key=lambda x: (-x[1],x[0]))


    make_tree(nodeinfo,0)
    answer.append(pre)
    answer.append(later)
    return answer

a=solution([[5,3]])
print(a)